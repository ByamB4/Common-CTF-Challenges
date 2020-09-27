Encoding decoding
-

* `Monks cipher`

	![https://github.com/ByamB4/Capture-The-Flag-Tools/blob/master/Cryptography/Images/Monks%20cipher/monks%20cipher.jpg](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cryptography/static/img/monks-cipher/table.jpg)
	
Transposition cipher
-

* `Rail Fence`

	* [https://www.dcode.fr/rail-fence-cipher](https://www.dcode.fr/rail-fence-cipher)
	
Substitution cipher
-

* `Vigenère cipher`
* `Fractionated Morse Cipher`
	* `BGJTWGVFFOEGJUPSHSLNTHDVLKI`
	
Asymmetric cryptography 
-

* `Rivest-Shamir–Adleman`

	* **wiener-attack** when given **e** is small.
	* `n1`, `n2`, `n3`, `c1`, `c2`, `c3` өгөгдсөн мөн `e=3` үед [CRT](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cryptography/src/asymmetric-cipher/rsa/small-e-with-values.py) хэрэгжүүлж болно.
	* [Brute force - encrypt 4 letter](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cryptography/src/asymmetric-cipher/rsa/brute-force-encrypt-4-letter.py)
	* [Brute force - encrypt e guessing](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cryptography/src/asymmetric-cipher/rsa/find-e.py)
	* [`c1`, `c2`, `e1`, `e2` given](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cryptography/src/asymmetric-cipher/rsa/common-modules-attack.py) 
	* [`p`, `q`, `e` өгөгдсөн үед `d` олох](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cryptography/src/asymmetric-cipher/rsa/p-q-e-given-calculate-d.py)
	
	Public key, Private key, Encrypted text base64-өөр өгөгдсөн үед дараах байдлаар бодож болно
	* `base64 -d < pub.b64 > pub.der`
	* `base64 -d priv.b64 | openssl rsa -inform DER > out.key`
	* `base64 -d enc.b64 > enc`
	* `openssl rsautl -decrypt -inkey out.key < enc > decrypted`
	
	Нийтлэг дайралтууд
	* `Hastad’s Broadcast Attack`
		
		* N1, N2, N3, C1, C2, C3 өгөгдсөн буюу e = 3 үед энэ нь боломжтой.
		* [python2](https://github.com/ByamB4/Capture-The-Flag-Tools/blob/master/Cryptography/RSA/Hasted's%20Attack.py)
		
	* `Fermat’s attack`
	
		* P, Q хоёр ижил урттай анхны тоо ч хэтэрхий ойрхон буюу ялгавар бага үед.
	
	* `Too many primes`
	
		* [Python2](https://github.com/ByamB4/Capture-The-Flag-Tools/blob/master/Cryptography/Code/rsa-too-many-primes.py)

Symmetric cryptography
-

* `Fernet`

	Mostly starts with **gAAAAABaDDCR** also cannot decrypt without key
	* [https://asecuritysite.com/encryption/ferdecode](https://asecuritysite.com/encryption/ferdecode)
	
Hash functions 
-

* `MD-5`
	
Block cipher 
-

* `AES-ECB`
	
	* [simple-python-3](https://github.com/ByamB4/CCC/blob/master/Cryptography/src/block-cipher/aes-ecb/simple-python-3.py)

