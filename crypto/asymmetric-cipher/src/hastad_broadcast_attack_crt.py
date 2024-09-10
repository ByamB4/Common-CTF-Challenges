from Crypto.Util.number import long_to_bytes as ltb

e = 0x3
n1 = 0xDEADBEEF
n2 = 0xDEADBEEF
n3 = 0xDEADBEEF
c1 = 0xDEADBEEF
c2 = 0xDEADBEEF
c3 = 0xDEADBEEF

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def find_invpow(x,n):
    high = 1
    while high ** n < x:
        high *= 2
    low = high / 2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x: low = mid
        elif high > mid and mid**n > x: high = mid
        else: return mid
    return mid + 1

flag_cubed = chinese_remainder([n1, n2, n3],[c1, c2, c3])
flag = find_invpow(flag_cubed, 3)

print(ltb(flag))
