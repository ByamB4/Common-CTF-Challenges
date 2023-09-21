## Frida

- Show installed apps

  - `frida-ps -Uai`

## Apktool

- Rebuild apk file

  ```bash
  apktool d [NAME].apk
  keytool -genkey -v -keystore release.keystore -alias release.keystore.alias -keyalg RSA -keysize 2048 -validity 3650
  ~/Library/Android/sdk/build-tools/30.0.3/apksigner sign --ks release.keystore [NAME].apk
  ```
