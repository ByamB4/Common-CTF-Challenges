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
  - `git clone https://github.com/P1sec/hermes-dec`
  - `python3 setup.py install`
  - `python3 hbc_disassembler.py [INPUT] disassemreact`
  - `python3 hbc_decompiler.py [INPUT] decompiledreact`

### TODO
  - [https://mas.owasp.org/crackmes/](https://mas.owasp.org/crackmes/)
