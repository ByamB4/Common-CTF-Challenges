from pwn import *

elf = context.binary = ELF('challenge', checksec=False)

context.log_level = 'debug'

io = process(elf.path)

io.sendline(cyclic(128))
io.wait()

core = io.corefile
stack = core.rsp
pattern = core.read(stack, 4)

success(f"Pattern: {pattern.decode()}")
success(f'Offset: {cyclic_find(pattern)}')
