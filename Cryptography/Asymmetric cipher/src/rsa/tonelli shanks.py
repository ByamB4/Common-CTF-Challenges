from Crypto.Util.number import long_to_bytes

n = 11183632493295722900188836927564142822637910363304123337597708503476804292242860556684644449701772313571249316546794463854991452685201761786385895405863639
c = 8939043592146774508422725937231398285333145869395369605787177287036646137314173055510198460479672008589091362568215564488685390459997440273900039337645280
e = 4


def legendre(a, p):
    return pow(a, (p - 1) // 2, p)


def tonelli(n, p):
    assert legendre(n, p) == 1, "not a square (mod p)"
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r


def find_square_roots(c, e):
    if e == 1:
        flag = long_to_bytes(c)
        if b"b00t2root" in flag:
            print(flag)
        return

    elif pow(c, (n-1)//2, n) != 1:
        return

    else:
        rt1 = tonelli(c, n)
        find_square_roots(rt1, e//2)
        rt2 = n - rt1
        find_square_roots(rt2, e//2)
    return


find_square_roots(c, e)
