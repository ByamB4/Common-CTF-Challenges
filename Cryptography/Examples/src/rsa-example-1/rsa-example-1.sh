echo "e8oQDihsmkvjT3sZe+EE8lwNvBEsFegYF6+OOFOiR6gMtMZxxba/bIgLUD8pV3yEf0gOOfHuB5bC3vQmo7bE4PcIKfpFGZBA" | openssl base64 -d > cipher2.cipher
./RsaCtfTool.py --publickey ./pubkey.pem --private > private.key
openssl rsautl -decrypt -inkey private.key < cipher2.cipher > decrypted
