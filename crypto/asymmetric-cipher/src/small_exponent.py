from Crypto.Util.number import long_to_bytes

c = 3708354049649318175189820619077599798890688075815858391284996256924308912935262733471980964003143534200740113874286537588889431819703343015872364443921848
e = 16
p = 75000325607193724293694446403116223058337764961074929316352803137087536131383
q = 69376057129404174647351914434400429820318738947745593069596264646867332546443

phi = (p - 1) * (q - 1)
n = p * q


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


g, yp, yq = egcd(p, q)

mp = pow(c, (p + 1) // 4, p)
mq = pow(c, (q + 1) // 4, q)

for i in range(3):
    mp = pow(mp, (p + 1) // 4, p)
    mq = pow(mq, (q + 1) // 4, q)

r = (yp * p * mq + yq * q * mp) % n
mr = n - r
s = (yp * p * mq - yq * q * mp) % n
ms = n - s
for num in [r, mr, s, ms]:
    print(long_to_bytes(num))
