from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes, inverse


n = 0xDEADBEEF
e = 0xDEADBEEF
c = 0xDEADBEEF

p = iroot(n, 2)
phi = p * (p - 1)
d = inverse(e, phi)
m = pow(c, d, n)

print(long_to_bytes(m))
