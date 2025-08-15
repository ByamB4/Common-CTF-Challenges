> No RELRO: Possible to overwrite global variable
> No canary: Possible to smash the stack
> NX disabled: Possible to write and execute from the stack
> No PIE: Virtual address it should use and keeps its memory layout quite static
> File descriptor: input: 0, output: 1, error: 2

- **Syscall table**

  - [`https://x64.syscall.sh/`](https://x64.syscall.sh/)
  - [`https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md`](https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md)

- **Libc offset**

  - [`https://libc.blukat.me/`](https://libc.blukat.me/)
  - [`https://libc.rip/`](https://libc.rip/)

- **Shellcode**

  - **Restricted (alphabets+digits)**
    - [https://github.com/TaQini/alpha3](https://github.com/TaQini/alpha3)
    
    - [https://github.com/SkyLined/alpha3/tree/master](https://github.com/SkyLined/alpha3/tree/master)

- **Interesting repo**
    - [https://github.com/TheFlash2k/flashlib/tree/main](https://github.com/TheFlash2k/flashlib/tree/main)
