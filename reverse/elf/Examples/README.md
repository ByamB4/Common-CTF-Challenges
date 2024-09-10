## Bypass ptrace

**Example 1:**

- Challenge: Bypass ptrace
- Solution:
  - Open with ghidra (raw binary)
  - Change **JNS** compare to **JMP** for disabling TEST instuction
- [source](https://github.com/ByamB4/CCC/blob/master/Cryptography/Examples/src/rsa-example-1.pem)
- [patched](https://github.com/ByamB4/CCC/blob/master/Cryptography/Examples/src/rsa-example-1.cipher)
