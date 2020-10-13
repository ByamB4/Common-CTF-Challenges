from owiener import attack
from Crypto.Util.number import long_to_bytes

N = 0xDEADBEEF
e = 0xDEADBEEF
c = 0xDEADBEEF
d = attack(e, N)

if d:
    print(long_to_bytes(pow(c, d, N)).decode())
else:
    print('No luck!')
