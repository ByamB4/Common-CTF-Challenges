- **Patch libc function**

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
      let blank = new NativeCallBack(() => {}, "void", []);
      Interceptor.replace(sleepfn, blank);
      ```
    - Execute binary and find process id
    - `frida -p <pid> -l agent.js`

  - Patch sleep function (during binary execution windows binary)

    - [writeup](https://docs.google.com/document/d/1Pls6AkWHbxvBuvDFLEv7piH9myZSahvQy4d3qR442Cw)

- **Extract python from binary**

  - [`pyinstxtractor`](https://github.com/extremecoders-re/pyinstxtractor)

- **Decompile `.pyc` file**

  - [`pylingual.io`](https://pylingual.io/)
  - [`pycdc`](https://github.com/zrax/pycdc)
  - `uncompyle6`
  - `decompyle3`
  - [`stegosaurus`](https://bitbucket.org/jherron/stegosaurus.git)

- **Capa**

  - The FLARE team's open-source tool to identify capabilities in executable files.

- **Detect It Easy**

  - Program for determining types of files for Windows, Linux and MacOS.

- **Process monitor filter**

  - Advanced monitoring tool for Windows that shows real-time file system, Registry and process/thread activity.

- **Godot**

  - [online-tool](https://github.com/bruvzg/gdsdecomp)
 
- **Lua**

  - [https://luadec.metaworm.site/](https://luadec.metaworm.site/)
 
- **Convert asm to binary**

  - `gcc -c chall.s -o chall.o -masm=intel`
