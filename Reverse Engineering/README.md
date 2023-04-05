### Patch libc function

- Patch sleep function

  - Create `nosleep.c`
    ```c
    #include <stdio.h>

    unsigned int sleep(unsigned int seconds) {
      return 0;
    }

    __attribute__((constructor)) static void setup(void){
      fprintf(stderr, "Hooked process,no sleeps!\n");
    }
    ```
  - Compile `gcc -shared -fPIC -ldl nosleep.c -o nosleep.so`
  - Execute `LD_PRELOAD="./nosleep.so" ./<binary>`

### Capa

- The FLARE team's open-source tool to identify capabilities in executable files.


### Detect It Easy

- Program for determining types of files for Windows, Linux and MacOS.

### Process monitor filter

- Advanced monitoring tool for Windows that shows real-time file system, Registry and process/thread activity.
