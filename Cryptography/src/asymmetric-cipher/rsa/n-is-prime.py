from Crypto.Util.number import inverse, long_to_bytes as ltb
from sympy import isprime
from pwn import log

n = 0xDEADBEEF
e = 0xDEADBEEF
c = 0XDEADBEEF

log.info('Checking N is prime')
if not isprime(n):
  log.warn('N is not prime number')
  exit()
log.success('N is prime')
d = inverse(e, n - 1)
m = pow(c, d, n)
log.info(f'd: {d}')
log.info(f'm: {m}')
log.success(f'flag: {ltb(m).decode()}')
