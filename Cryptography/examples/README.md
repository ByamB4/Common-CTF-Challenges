## RSA

**Example 1:**

- Challenge: Cipher text given as base64, public key given as .pem
- Solution:
  - Decode cipher text using openssl base64
  - Export private key using RsaCtfTool
  - Decrypt message using openssl.
- [pub-key.pem](https://github.com/ByamB4/CCC/blob/master/Cryptography/examples/src/rsa-example-1.pem)
- [cipher](https://github.com/ByamB4/CCC/blob/master/Cryptography/examples/src/rsa-example-1.cipher)
- [solution](https://github.com/ByamB4/CCC/blob/master/Cryptography/examples/src/rsa-example-1.sh)

```sh
echo "e8oQDihsmkvjT3sZe+EE8lwNvBEsFegYF6+OOFOiR6gMtMZxxba/bIgLUD8pV3yEf0gOOfHuB5bC3vQmo7bE4PcIKfpFGZBA" | openssl base64 -d > cipher2.cipher
./RsaCtfTool.py --publickey ./pubkey.pem --private > private.key
openssl rsautl -decrypt -inkey private.key < cipher2.cipher > decrypted
```

**Example 2:**

- Challenge: Two different e, c. Same n. Also known as Common modules.
- Solution:
  - Write python script
- [key1_pub.pem](https://github.com/ByamB4/CCC/blob/master/Cryptography/examples/src/rsa-example-1.pem)
- [key2_pub.pem](https://github.com/ByamB4/CCC/blob/master/Cryptography/examples/src/rsa-example-1.cipher)
- [message1]
- [message2](https://github.com/ByamB4/CCC/blob/master/Cryptography/examples/src/rsa-example-1.sh)
- [solution](https://github.com/ByamB4/CCC/blob/master/Cryptography/examples/src/rsa-example-1.sh)
