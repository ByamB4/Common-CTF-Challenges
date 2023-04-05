### Patch libc function

- Patch sleep function (before binary execute)

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

- Patch sleep function (during binary execution)

  - Create `agent.js`
    ```js
    let sleepfn = Module.findExportByName("libc.so.6", "sleep");
    let blank = new NativeCallBack(() => {}, 'void', []);
    Interceptor.replace(sleepfn, blank)
    ```
  - Execute binary and find process id
  - `frida -p <pid> -l agent.js`



### Capa

- The FLARE team's open-source tool to identify capabilities in executable files.


### Detect It Easy

- Program for determining types of files for Windows, Linux and MacOS.

### Process monitor filter

- Advanced monitoring tool for Windows that shows real-time file system, Registry and process/thread activity.
