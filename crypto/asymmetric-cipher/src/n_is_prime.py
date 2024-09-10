from Crypto.Util.number import inverse, long_to_bytes
from sympy import isprime

n = 0xDEADBEEF
e = 0xDEADBEEF
c = 0xDEADBEEF

if not isprime(n):
    print("N is not prime number")
    exit()
d = inverse(e, n - 1)
m = pow(c, d, n)
print(long_to_bytes(m))
