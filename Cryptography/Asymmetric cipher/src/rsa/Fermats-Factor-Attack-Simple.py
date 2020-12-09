from Crypto.Util.number import long_to_bytes as ltb, inverse
from gmpy2 import isqrt, square, is_square

n = REDACTED
e = REDACTED
c = REDACTED

def fermat_factors(n):
    assert n % 2 != 0
    a = isqrt(n)
    b2 = square(a) - n
    while not is_square(b2):
        a += 1
        b2 = square(a) - n
    factor1 = a + isqrt(b2)
    factor2 = a - isqrt(b2)
    return int(factor1), int(factor2)

p, q = fermat_factors(n)
d = inverse(e, (p - 1) * (q - 1))
m = pow(c, d, n)

print(ltb(m))
