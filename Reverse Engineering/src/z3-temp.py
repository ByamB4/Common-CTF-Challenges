from z3 import *

_b = [ BitVec(f'{i}', 8) for i in range(8) ]
_i = [ Int(f'{i}') for i in range(8) ]
print('[+] Trying to prove')
s = Solver()

# -- Stage 1 --
s.add(_b[0] == 110)
s.add(_b[4] == 51)

s.add(Or(And(_b[1] >= 48, _b[1] <= 57), And(_b[1] >= 65, _b[1] <= 122)))
s.add(Or(And(_b[2] >= 48, _b[2] <= 57), And(_b[2] >= 65, _b[2] <= 122)))
s.add(Or(And(_b[3] >= 48, _b[3] <= 57), And(_b[3] >= 65, _b[3] <= 122)))
s.add(Or(And(_b[5] >= 48, _b[5] <= 57), And(_b[5] >= 65, _b[5] <= 122)))
s.add(Or(And(_b[6] >= 48, _b[6] <= 57), And(_b[6] >= 65, _b[6] <= 122)))
s.add(Or(And(_b[7] >= 48, _b[7] <= 57), And(_b[7] >= 65, _b[7] <= 122)))

# -- Stage 2 --
s.add(_b[0] + _b[1] + _b[2] + _b[3] + _b[4] + _b[5] + _b[6] + _b[7] == 0x287)
s.add(_b[0] * _b[1] * _b[2] * _b[3] * _b[4] * _b[5] * _b[6] * _b[7] == 0x39ded83f87480)
s.add(_b[0] ^ _b[1] ^ _b[2] ^ _b[3] ^ _b[4] ^ _b[5] ^ _b[6] ^ _b[7] == 0x3b)

# -- Stage 3 --
s.add(_b[1] + _b[2] + _b[4] + _b[5] == 0xce)


# -- Stage 4 --
s.add(_b[0] ^ _b[1] ^ _b[2] ^ _b[3] == 0x36)
s.add(_b[4] ^ _b[5] ^ _b[6] ^ _b[7] == 0xd)
s.add(_b[1] ^ _b[3] ^ _b[5] ^ _b[7] == 0x22)

# -- Custom --

if s.check() == sat:
    print("[+] Proved")
    print(s.model())
else:
    print("[-] Failed")
