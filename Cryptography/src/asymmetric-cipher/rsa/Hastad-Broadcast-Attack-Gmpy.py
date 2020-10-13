from Crypto.Util.number import long_to_bytes as ltb
from gmpy import invert, root

e = 0x3

n1 = 0xDEADBEEF
n2 = 0xDEADBEEF
n3 = 0xDEADBEEF

c1 = 0xDEADBEEF
c2 = 0xDEADBEEF
c3 = 0xDEADBEEF

N = n1 * n2 * n3
N1 = N / n1
N2 = N / n2
N3 = N / n3

u1 = invert(N1, n1)
u2 = invert(N2, n2)
u3 = invert(N3, n3)

M = (c1 * u1 * N1 + c2 * u2 * N2 + c3 * u3 * N3) % N

m = root(M,e)[0]

print(ltb(m))
