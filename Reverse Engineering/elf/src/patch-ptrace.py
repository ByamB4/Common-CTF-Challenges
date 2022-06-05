from pwn import *

binary = 'binary'
elf = context.binary = ELF(binary, checksec=False)

elf.asm(elf.symbols.ptrace, 'ret')

elf.save('patched')
