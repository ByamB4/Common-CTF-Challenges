from gmpy2 import *
from Crypto.Util.number import long_to_bytes as ltb

get_context().precision=2048

n = 0xDEADBEEF
e = 0xDEADBEEF
c = 0xDEADBEEF

p = int(root(n, 2))
phi = p * (p - 1)
d = invert(e, phi)
m = pow(c, d, n)

print(ltb(m))
