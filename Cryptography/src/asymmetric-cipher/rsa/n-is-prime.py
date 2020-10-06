from pwn import log
from sympy isprime

N = REDACTED

log.info('Checking N is prime')
if not isprime(N):
  log.warn('N is not prime number')
  exit()
