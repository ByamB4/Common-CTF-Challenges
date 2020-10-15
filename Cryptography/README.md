## Transposition Cipher

- [`Rail Fence (Zig-Zag) Cipher`](https://www.dcode.fr/rail-fence-cipher)

  - `FEPLOCLGXMLFAFRCAAEGC`

- [`Route/Path Cipher`](https://www.dcode.fr/route-cipher)
  - `DCODUORETECIREHP`
  
- [`Read more`](https://github.com/ByamB4/CCC/tree/master/Cryptography/Substitution%20Cipher)

## Hash function
  
  - Message Digest algorithm - 5
     - Length: 32

  - Secure Hash algorithm - 256
    - Length: 64

## Substitution Cipher

- [`Fractionated Morse Cipher`](https://www.dcode.fr/fractionated-morse)
  - `BGJTWGVFFOEGJUPSHSLNTHDVLKI`

## Poly-Alphabetic Cipher

- [`Vigenere Cipher`](https://www.dcode.fr/vigenere-cipher)
  - `nGmni Tskcxipo esdskkxgmejvc`

## Asymmetric Cryptography

- [`Rivest-Shamir–Adleman`](https://github.com/Ganapati/RsaCtfTool)
  - [Brute force - encrypt 4 letter](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cryptography/src/asymmetric-cipher/rsa/brute-force-encrypt-4-letter.py)
  - [Brute force - encrypt e guessing](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cryptography/src/asymmetric-cipher/rsa/find-e.py)
  - [`c1`, `c2`, `e1`, `e2` given](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cryptography/src/asymmetric-cipher/rsa/common-modules-attack.py)
  - [`p`, `q`, `e` given find `d`](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cryptography/src/asymmetric-cipher/rsa/p-q-e-given-calculate-d.py)
  - [`N is prime`](https://github.com/ByamB4/CCC/blob/master/Cryptography/src/asymmetric-cipher/rsa/n-is-prime.py)
  - [`N can be sqrt`](https://github.com/ByamB4/CCC/blob/master/Cryptography/src/asymmetric-cipher/rsa/sqrted-n.py)
  
  - `base64 -d < pub.b64 > pub.der`
  - `base64 -d priv.b64 | openssl rsa -inform DER > out.key`
  - `base64 -d enc.b64 > enc`
  - `openssl rsautl -decrypt -inkey out.key < enc > decrypted`

  Common attacks
  
  - `Small exponent`
  
      - [Find n-th root using gmpy](https://github.com/ByamB4/CCC/blob/master/Cryptography/src/asymmetric-cipher/rsa/small-exponent-attack-gmpy.py)
      
  - `Big exponent`
      
      - **n** is too big then public exponent **e** must be small.
      - [Wiener's attack](https://github.com/ByamB4/CCC/blob/master/Cryptography/src/asymmetric-cipher/rsa/Wiener-Attack.py)
      - [Boneh Durfee](https://someurl)
      
  - `Hastad’s Broadcast Attack`

    - **e** cipher text, with same **message**.
    - [Chinese remainder theorem](https://github.com/ByamB4/CCC/blob/master/Cryptography/src/asymmetric-cipher/rsa/Hastad-Broadcast-Attack-CRT.py)
    - [Simple gmpy](https://github.com/ByamB4/CCC/blob/master/Cryptography/src/asymmetric-cipher/rsa/Hastad-Broadcast-Attack-Gmpy.py)
    
  - `Fermat's attack`

    - **p**, **q** is too near, also known as difference is small.
    - [Fermat factor](https://github.com/ByamB4/CCC/blob/master/Cryptography/src/asymmetric-cipher/rsa/Fermats-Factor-Attack-Simple.py)

  - `Too many primes`

    - [Python2](https://github.com/ByamB4/Capture-The-Flag-Tools/blob/master/Cryptography/Code/rsa-too-many-primes.py)

## Symmetric cryptography

- [`Fernet`](https://asecuritysite.com/encryption/ferdecode)

  `Token: gAAAAABWC9P7-9RsxTz_dwxh9-O2VUB7Ih8UCQL1_Zk4suxnkCvb26Ie4i8HSUJ4caHZuiNtjLl3qfmCv_fS3_VpjL7HxCz7_Q==`
  `Key: -s6eI5hyNh8liH7Gq0urPC-vzPgNnxauKvRO4g03oYI=`

## Block cipher

- `AES-ECB`

  - [simple-python-3](https://github.com/ByamB4/CCC/blob/master/Cryptography/src/block-cipher/aes-ecb/simple-python-3.py)
