from Crypto.Util.number import long_to_bytes as ltb, inverse
import gmpy2

n = REDACTED
e = REDACTED
c = REDACTED

def fermat_factors(n):
    assert n % 2 != 0
    a = gmpy2.isqrt(n)
    b2 = gmpy2.square(a) - n
    while not gmpy2.is_square(b2):
        a += 1
        b2 = gmpy2.square(a) - n
    factor1 = a + gmpy2.isqrt(b2)
    factor2 = a - gmpy2.isqrt(b2)
    return int(factor1), int(factor2)

p, q = fermat_factors(n)
d = inverse(e, (p - 1) * (q - 1))
m = pow(c, d, n)

print(ltb(m))
