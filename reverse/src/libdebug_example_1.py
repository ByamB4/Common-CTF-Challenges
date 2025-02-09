from pwn import *
from libdebug import debugger
import numpy as np
import string

candidates = string.ascii_letters + string.digits + string.punctuation

# We have 23 SBOXes, each of which maps len(candidates) to some byte value.
sboxes = np.zeros((23, len(candidates)), dtype=np.uint8)

# Now, for each candidate, we check what it is masked to at each index.
for i, candidate in enumerate(candidates):
    p = process("./inner_resym.elf")
    d = debugger("./inner_resym.elf")
    d.attach(p.proc.pid)
    # We set a breakpoint just after our data was loaded into xmm0/xmm1
    d.breakpoint(0x8e30, file="binary")
    d.cont()

    # Send the candidate for every index
    p.sendline(str(candidate).encode()*23)

    # Wait for the breakpoint to be hit
    d.wait()

    # Now get the SBOX result at each index
    first_16_bytes = d.regs.xmm0.to_bytes(16, "little")
    last_16_bytes = d.regs.xmm1.to_bytes(16, "little")
    all_masked = first_16_bytes + last_16_bytes[9:]
    sboxes[:,i] = list(all_masked)

    d.detach()
    p.close()
