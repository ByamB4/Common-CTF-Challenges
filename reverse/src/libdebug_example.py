import subprocess
import time
from libdebug import debugger

known_flag = b""
sboxes = []
for i in range(23):
    sboxes.append([])

for i in range(33, 128):
    didnt_work = True
    while didnt_work:
        known_flag = bytes([i]) * 23
        proc = subprocess.Popen(
            ["./binary.bin-patched"], 
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )
        pid = proc.pid
        time.sleep(0.1)

        d = debugger("./binary.bin-patched")
        d.attach(pid)
        d.breakpoint(0x8E27, file="binary", hardware=False)
        proc.stdin.write(known_flag + b"\n")
        proc.stdin.flush()
 
        d.cont()
        if d.regs.rip & 0xE27:
            enc = d.regs.rbx
            for i in range(23):
                sboxes[i].append(int.from_bytes(d.memory[enc+i:enc+i+1]))
            didnt_work = False
        else:
            d.kill()
            proc.close()

enc = bytes.fromhex("2205E10F65121BCA0FF5E18D3FF3E7A5")
enc = enc[::-1]
enc2 = bytes.fromhex("0F CA 1B 12 65 0F E1 05 22 0F CF 14 36 E8 3C 3A")
enc2 = enc2[9:]
enc += enc2
flag = ""
for i in range(len(enc)):
    sbox = sboxes[i]
    flag += chr(sbox.index(enc[i])+33)
    print(flag)
