# Mobile

Android-focused reversing and runtime manipulation notes.

## Quick wins

- Pull or rebuild the APK quickly (adb + apktool) and re-sign before installing.
- Use Frida for runtime hooks; start the server on device/emulator and attach with `frida-ps -Uai`.
- For React Native/Hermes bundles, disassemble/decompile with hermes-dec to recover JS.

## Frida

- Run server on device: `cd /data/local/tmp; ./frida-server &`
- List installed apps: `frida-ps -Uai`
- Call function example script: `reverse/src/frida_call_function.js`
- Trace function calls: https://codeshare.frida.re/@d3z3n0v3/trace-function-calls/
- Hook package example: `frida -U -f mn.chall.flag -l hook.js`

## APK rebuild and resign

```
keytool -genkey -v -keystore key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias chall
apktool d app.apk
apktool b app -o updated.apk
apksigner sign --ks key.jks updated.apk
# alternative signer: https://github.com/patrickfav/uber-apk-signer
```

## Extracting APKs

- Method 1 (ML Manager): install ML Manager, then `adb pull "/storage/emulated/0/Android/media/com.javiersantos.mlmanager/<APK_NAME>"`
- Method 2 (adb):
  ```
  adb shell pm list packages
  adb shell pm path com.application.example
  adb pull /data/app/~~igIDWXFnPHEQj1nabZV0yQ==/com.application.example-*/base.apk ./output.apk
  ```

## Split APKs (.apks)

```
unzip app.apks -d apks
adb install-multiple ./apks/*.apk
```

## Hermes bytecode (React Native)

```
git clone https://github.com/P1sec/hermes-dec
cd hermes-dec && python3 setup.py install
python3 hbc_disassembler.py index.android.bundle disassembled_hermes
python3 hbc_decompiler.py index.android.bundle decompiled_hermes
```

## Anti-debug / ptrace note

- If ptrace is blocking you, patch the check (e.g., change JNS to JMP) or attach after a `ptrace(0,0,0,0)` returns.

## SSL pinning bypass options

- HTTP Toolkit + Burp: https://httptoolkit.com/blog/android-https-mitm-art-of-pinning/
  - Install HTTP Toolkit on-device, route traffic via Burp, trust the Burp cert, let HTTP Toolkit handle unpinning hooks.
- Frida unpinning scripts: run universal hooks (e.g., `frida-android-unpinning`) to override common trust managers.
- System trust (root/emulator): install Burp/Charles CA into system store or use Magisk modules (e.g., `trustusercerts`) to accept user CAs globally.
