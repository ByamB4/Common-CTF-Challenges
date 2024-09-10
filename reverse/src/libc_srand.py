import ctypes

srand = 0x1337
print(f"{srand=}")

libc = ctypes.CDLL("libc.so.6")
libc.srand(srand)
print(libc.rand() % 3)
