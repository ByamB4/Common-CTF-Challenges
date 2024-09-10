from Crypto.Util.number import long_to_bytes

def tonelli_shanks(n, p):
    """ Tonelli-Shanks algorithm to find modular square root of n modulo p """
    if pow(n, (p - 1) // 2, p) != 1:
        return None
    
    if p == 2:
        return n % 2
    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)

    s = 0
    q = p - 1
    while q % 2 == 0:
        s += 1
        q //= 2

    z = 2
    while pow(z, (p - 1) // 2, p) == 1:
        z += 1

    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q + 1) // 2, p)

    while t != 0 and t != 1:
        t2i = t
        i = 0
        for i in range(1, m):
            t2i = pow(t2i, 2, p)
            if t2i == 1:
                break
        b = pow(c, 2 ** (m - i - 1), p)
        m = i
        c = pow(b, 2, p)
        t = (t * c) % p
        r = (r * b) % p

    return r if t == 1 else None

def crt(a, n):
    """ Chinese Remainder Theorem implementation """
    x = 0
    M = 1
    for mod in n:
        M *= mod
    for ai, ni in zip(a, n):
        Mi = M // ni
        inv = pow(Mi, -1, ni)
        x = (x + ai * Mi * inv) % M
    return x

# Given values
p = 206639924717418437401035938473738891291
q = 275851500244078118973600867404796177479
c = 27935842515331188568739284081168109107146364158293266475077147278541420202373
e = 2

# Calculate n
n = p * q

# Compute the square roots modulo p and q
sqrt_p_pos = tonelli_shanks(c, p)
sqrt_p_neg = p - sqrt_p_pos if sqrt_p_pos else None
sqrt_q_pos = tonelli_shanks(c, q)
sqrt_q_neg = q - sqrt_q_pos if sqrt_q_pos else None

# Print intermediate results
print("Square root modulo p:", sqrt_p_pos, sqrt_p_neg)
print("Square root modulo q:", sqrt_q_pos, sqrt_q_neg)

# Handle possible roots
roots_p = [sqrt_p_pos, sqrt_p_neg] if sqrt_p_pos else []
roots_q = [sqrt_q_pos, sqrt_q_neg] if sqrt_q_pos else []

# Check all combinations using CRT
congruences = []
for rp in roots_p:
    for rq in roots_q:
        congruences.append((rp, rq))

solutions = []
for congruence in congruences:
    try:
        x = crt(congruence, [p, q])
        solutions.append(x)
    except Exception as e:
        print(f"CRT Error: {e}")

# Print solutions
print("Possible solutions:", solutions)

# Decrypt the ciphertext
if solutions:
    m = solutions[0]
    plaintext = long_to_bytes(int(m))
    try:
        flag = plaintext.decode()
        if flag.startswith("HRC-CTF{") and flag.endswith("}"):
            print("Flag:", flag)
        else:
            print("Invalid format:", flag)
    except UnicodeDecodeError:
        print("Unable to decode plaintext")
else:
    print("No valid solution found")
