from owiener import attack
from Crypto.Util.number import long_to_bytes

n = 0xDEADBEEF
e = 0xDEADBEEF
c = 0xDEADBEEF
d = attack(e, n)

if d:
    print(long_to_bytes(pow(c, d, n)).decode())
else:
    print('No luck!')
