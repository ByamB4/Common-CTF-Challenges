# Pwn

Binary exploitation reminders and quick references.

## Quick wins
- Check protections first: RELRO, canary, NX, PIE, file descriptors.
- Identify the libc version/offsets early to avoid wrong gadgets.
- For restricted shellcode (alphanumeric), use dedicated encoders.

## Protections cheatline
- No RELRO: overwrite GOT/global variables possible.
- No canary: stack smashing is viable.
- NX disabled: stack/executable segments writable+executable.
- No PIE: addresses stay static; hardcode libc/PLT.
- File descriptors: stdin 0, stdout 1, stderr 2.

## References
- Syscall tables: https://x64.syscall.sh/, https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md
- Libc offsets: https://libc.blukat.me/, https://libc.rip/
- Alphanumeric shellcode encoders: https://github.com/TaQini/alpha3, https://github.com/SkyLined/alpha3/tree/master
- Exploit library repo: https://github.com/TheFlash2k/flashlib/tree/main
