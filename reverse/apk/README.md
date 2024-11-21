## Frida

- Run server
  - `cd /data/local/tmp; ./frida-server &`
  
- Show installed apps
  - `frida-ps -Uai`
 
- Call function
  - [frida.js](https://github.com/ByamB4/Common-CTF-Challenges/blob/main/reverse/src/frida_call_function.js)

### Rebuilding apk file

  - `keytool -genkey -v -keystore key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias chall` 
  - `apktool d [INPUT].apk`
  - `apktool b [FOLDER_NAME] -o updated.apk`
  - `apksigner sign --ks key.jks updated.apk`
  - [uber-apk-signer](https://github.com/patrickfav/uber-apk-signer)
