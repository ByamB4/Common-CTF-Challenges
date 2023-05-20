from Crypto.Util.number import long_to_bytes
from gmpy2 import invert, iroot

e = 0x3

n1 = 0x0
n2 = 0x0
n3 = 0x0

c1 = 0x0
c2 = 0x0
c3 = 0x0

N = n1 * n2 * n3
N1 = N // n1
N2 = N // n2
N3 = N // n3

u1 = invert(N1, n1)
u2 = invert(N2, n2)
u3 = invert(N3, n3)

M = (c1 * u1 * N1 + c2 * u2 * N2 + c3 * u3 * N3) % N

m = iroot(M,e)[0]

print(long_to_bytes(m))
