- `Python code packed`

  Extract python code from binary

  - `pyi-archive_viewer` Extract the .pyc file
  - `uncompyle6` To uncompile .pyc file

- `Bypassing ptrace`

  - `Ghidra` open with raw binary, change **JNS** compare to **JMP** for disabling TEST instuction.

- `Bypassing strcmp`

  - Method 1: - Write own strcmp function then attach
    ```c
    #include <stdio.h>
    int strcmp (const char* s1, const char* s2) {
      printf("s1: %s\n", s1);
      printf("s2: %s\n", s2);
      return 0;
    }
    ```
    ```sh
    gcc -fPIC -c strcmp.c -m32 -o strcmp.o
    gcc -shared -o strcmp.so strcmp.o -m32
    $gdb➤  set environment LD_PRELOAD ./strcmp.so
    ```
