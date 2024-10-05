## Frida

- Show installed apps

  - `frida-ps -Uai`

## Apktool

- Rebuild apk file

  ```bash
  apktool d [NAME].apk
  apktool b [FOLDER] -o updated.apk
  keytool -genkey -v -keystore key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias chall
  apksigner sign --ks key.jks updated.apk
  ```
