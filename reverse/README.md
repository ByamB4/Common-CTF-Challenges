### Python

- Reversing Compiled Python `(.pyc)`

  - [pylingual.io](https://pylingual.io/)
 
  - [pycdc](https://github.com/zrax/pycdc)
 
  - [https://github.com/rocky/python-uncompyle6](https://github.com/rocky/python-uncompyle6)
    
  - [https://github.com/rocky/python-decompile3](https://github.com/rocky/python-decompile3)
    
  - [https://bitbucket.org/jherron/stegosaurus.git](https://bitbucket.org/jherron/stegosaurus.git)

### Rust/Go

- [https://github.com/h311d1n3r/Cerberus](https://github.com/h311d1n3r/Cerberus)

### Tricks

- **Resource editor**
  - [https://www.resource-editor.com/](https://www.resource-editor.com/)

- **Convert asm to binary**

  - `gcc -c chall.s -o chall.o -masm=intel`

- **Capa**

  - The FLARE team's open-source tool to identify capabilities in executable files.

- **Detect It Easy**

  - Program for determining types of files for Windows, Linux and MacOS.

- **Process monitor filter**

  - Advanced monitoring tool for Windows that shows real-time file system, Registry and process/thread activity.

### Godot

- [https://godotengine.org/download/windows/](https://godotengine.org/download/windows/)
- [https://github.com/bruvzg/gdsdecomp](https://github.com/bruvzg/gdsdecomp)
- [writeup-1](https://medium.com/@Sle3pyHead/the-game-ctf-notes-tryhackme-babeb48c2ae9)

### Lua

- [https://luadec.metaworm.site/](https://luadec.metaworm.site/)

## Frida

- Run server
  - `cd /data/local/tmp; ./frida-server &`
- Show installed apps

  - `frida-ps -Uai`

- Call function

  - [frida.js](https://github.com/ByamB4/Common-CTF-Challenges/blob/main/reverse/src/frida_call_function.js)

- Trace function calls
  - [https://codeshare.frida.re/@d3z3n0v3/trace-function-calls/](https://codeshare.frida.re/@d3z3n0v3/trace-function-calls/)

### Rebuilding apk file

- `keytool -genkey -v -keystore key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias chall`
- `apktool d [INPUT].apk`
- `apktool b [FOLDER_NAME] -o updated.apk`
- `apksigner sign --ks key.jks updated.apk`
- [uber-apk-signer](https://github.com/patrickfav/uber-apk-signer)

### Hook function

- `frida -U -f mn.chall.flag -l hook.js`

### Extract apk from installed application (emulator)

- `adb shell pm list packages`
- `adb shell pm path [com.application.example]`
- `adb pull [/data/app/~~igIDWXFnPHEQj1nabZV0yQ==/com.application.example-f0FVENe4Co6LNpL-usLWbg==/base.apk] ./output.apk`

### Hermes bytecode

If `index.android.bundle` isn’t readable and it’s likely Hermes bytecode, the compiled form of React Native’s JavaScript. You can disassemble or decompile it using `hermes-dec`

```bash
# clone and install hermes-dec
git clone https://github.com/P1sec/hermes-dec
cd hermes-dec
python3 setup.py install

# disassemble or decompile Hermes bytecode
python3 hbc_disassembler.py index.android.bundle disassembled_hermes
python3 hbc_decompiler.py index.android.bundle decompiled_hermes
```

## Bypass ptrace

- Challenge: Bypass ptrace
- Solution:
  - Open with ghidra (raw binary)
  - Change **JNS** compare to **JMP** for disabling TEST instuction

## UPX Packed

Sometime UPX packed binary can't decompressed back. So author is manually changed some byte or even sections.

- You can try to guess
- Missing library. Append kernel32.dll to actual binary. [code](https://github.com/ByamB4/CCC/blob/master/Reverse%20Engineering/exe/src/append-kernel32.py)

## Python code packed

Extract python code from binary

- [PyInstallerExtractor](https://github.com/extremecoders-re/pyinstxtractor) Python script to extract the contents of a PyInstaller generated Windows executable file.

## Unity

- [https://dnspy.org/](https://dnspy.org/)
- [https://github.com/AssetRipper/AssetRipper](https://github.com/AssetRipper/AssetRipper)


### TODO

- [https://mas.owasp.org/crackmes/](https://mas.owasp.org/crackmes/)
