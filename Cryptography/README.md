## Transposition Cipher

- `Rail Fence (Zig-Zag) Cipher`

  - [`FEPLOCLGXMLFAFRCAAEGC`](https://www.dcode.fr/rail-fence-cipher)

- `Route/Path Cipher`
  - [`DCODUORETECIREHP`](https://www.dcode.fr/route-cipher)

## Substitution Cipher

- `Fractionated Morse Cipher`
  - `BGJTWGVFFOEGJUPSHSLNTHDVLKI`

## Poly-Alphabetic Cipher

- `Vigenere Cipher`
  - `nGmni Tskcxipo esdskkxgmejvc`

## Asymmetric Cryptography

- `Rivest-Shamir–Adleman`

  - **wiener-attack** when given **e** is small.
  - `n1`, `n2`, `n3`, `c1`, `c2`, `c3` өгөгдсөн мөн `e=3` үед [CRT](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cryptography/src/asymmetric-cipher/rsa/small-e-with-values.py) хэрэгжүүлж болно.
  - [Brute force - encrypt 4 letter](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cryptography/src/asymmetric-cipher/rsa/brute-force-encrypt-4-letter.py)
  - [Brute force - encrypt e guessing](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cryptography/src/asymmetric-cipher/rsa/find-e.py)
  - [`c1`, `c2`, `e1`, `e2` given](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cryptography/src/asymmetric-cipher/rsa/common-modules-attack.py)
  - [`p`, `q`, `e` given find `d`](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cryptography/src/asymmetric-cipher/rsa/p-q-e-given-calculate-d.py)

  Given file as base64

  - `base64 -d < pub.b64 > pub.der`
  - `base64 -d priv.b64 | openssl rsa -inform DER > out.key`
  - `base64 -d enc.b64 > enc`
  - `openssl rsautl -decrypt -inkey out.key < enc > decrypted`

  Common attacks

  - `Hastad’s Broadcast Attack`

    - N1, N2, N3, C1, C2, C3 given also e = 3.
    - [python2](https://github.com/ByamB4/Capture-The-Flag-Tools/blob/master/Cryptography/RSA/Hasted's%20Attack.py)

  - `Fermat’s attack`

    - P, Q too near as N also known as difference is small.

  - `Too many primes`

    - [Python2](https://github.com/ByamB4/Capture-The-Flag-Tools/blob/master/Cryptography/Code/rsa-too-many-primes.py)

## Symmetric cryptography

- `Fernet`

  Mostly starts with **gAAAAABaDDCR** also cannot decrypt without key

  - [https://asecuritysite.com/encryption/ferdecode](https://asecuritysite.com/encryption/ferdecode)

## Block cipher

- `AES-ECB`

  - [simple-python-3](https://github.com/ByamB4/CCC/blob/master/Cryptography/src/block-cipher/aes-ecb/simple-python-3.py)
