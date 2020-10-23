# (a > 0 && a < 1000000) & (b > 0 && b < 1000000) & (c > 0 && c < 1000000)
for a in range(1, 1000000):
    for b in range(1, 1000000):
        d = a ** 3 + b ** 3
        if d > 999997000002999999:
            break
        if pow(d, 1.0/3.0) == int(pow(d, 1.0/3.0)):
            if a ** 3 + b ** 3 == pow(d, 1.0/3.0):
                print('found')
                print(a, b, d)
                input()
    print(a, b)
