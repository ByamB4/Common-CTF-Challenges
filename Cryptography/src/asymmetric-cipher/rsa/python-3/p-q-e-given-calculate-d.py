def egcd(a, b):
    if a == 0: return b, 0, 1
    else: g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1: raise Exception('Modular inverse does not exist')
    else: return x % m

if __name__ == '__main__':
    p, q, e = 0, 0, 0

    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)
    print(d)
