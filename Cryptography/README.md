Encoding decoding
-----------------------

* `Monks cipher`

	![https://github.com/ByamB4/Capture-The-Flag-Tools/blob/master/Cryptography/Images/Monks%20cipher/monks%20cipher.jpg](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cryptography/static/img/monks-cipher/table.jpg)
	
Transposition cipher
-----------------------

* `Rail Fence`

	* [https://www.dcode.fr/rail-fence-cipher](https://www.dcode.fr/rail-fence-cipher)
	
Substitution cipher
-----------------------

* `Vigenère cipher`

	* [https://www.guballa.de/vigenere-solver](https://www.guballa.de/vigenere-solver)

	
Asymmetric cryptography 
-----------------------

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
----------------------

* `Fernet`

	Mostly starts with **gAAAAABaDDCR** also cannot decrypt without key
	* [https://asecuritysite.com/encryption/ferdecode](https://asecuritysite.com/encryption/ferdecode)
	
Hash functions 
-----------------------

Hash нь ямар нэгэн мэдээллийн бүрэн бүтэн байдал, эх файл мөн эсэхийг шалгахад ихэвчлэ ашиглана. Дотроо хэд хэдэн тусдаа алгоритм байх бөгөөд хоорондоо битийн урт, бодож байгаа алгоритмаараа ялгаатай байна. Hash нь нэг зүгт нууцлалт бөгөөд эргүүлж задлана гэсэн ойлголт байхгүй, боломжит ганц арга нь **brute-force** билээ.

* `Message-Digest algorithm also MD5`
	128 бит урттай бөгөөд 16 байт гэсэн үг. Ингэснээр 32 ийн урттай hex утга гаргаж авна. 
	* `9e107d9d372bb6826bd81d3542a419d6`
	* [https://crackstation.net/](https://crackstation.net/)

	
Block cipher 
-

* `AES-ECB`
	
	ECB буюу Electronic Codebook нь plaintext-ийг тэнцүү урттай хэд хэдэн блок болгон хувааж нэг ижил түлхүүрээр нууцладаг. 
	
	![AES-Electronic codebook encryption image](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cryptography/static/img/block-cipher/aes-ecb/encryption.png)
	
	Буцааж задлахдаа яг ижил зарчмаар задлана. 
	
	![AES-Electronic codebook decryption image](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cryptography/static/img/block-cipher/aes-ecb/decryption.png)
	
	Тэгэхээр бид түлхүүрийг олохоос илүү аль нэг блок дээр байгаа текстийг нэг унших нь илүү үр дүнтэй юм. 

```
   'Agent,\nGreetings'    <--- 16  (Блок 1)
   '. My situation r'     <--- 16  (Блок 2)
   'eport is as foll'     <--- 16  (Блок 3)
   'ows:\nAAAAAAAAAAA'    <--- 16  (Блок 4)    <--- Оролт эхлэх хэсэг 
   'BBBBBBBBBBBBBBBB'     <--- 16  (Блок 5)    <--- padding 
   'CCCCCCCCCCCCCCCC'     <--- 16  (Блок 6) 
   '\nMy agent identi'    <--- 16  (Блок 7)
   'fying code is:  '     <--- 16  (Блок 8)    <--- мэдэгдэж буй блок
   'flagCTF{ABCDEFG}'     <--- 16  (Блок 9)    <--- бидний бай (ABCDEFG нь гүйцээж байгаа)
   '.Down with the S'  	  <--- 16  (Блок 10)   <--- мэдэгдэж буй блок
```
Бид эндээс Блок 6 ийн нэг тэмдэгтийг хасвал манай флагийн нэг тэмдэгт дээшээ гарч ирнэ. 

```
   'Agent,\nGreetings'    <--- 16  (Блок 1)
   '. My situation r'     <--- 16  (Блок 2)
   'eport is as foll'     <--- 16  (Блок 3)
   'ows:\nAAAAAAAAAAA'    <--- 16  (Блок 4)
   'ying code is:  %c'    <--- 16  (Блок 5)    <--- %c тэмдэгт[32-128] хүртэл Блок 8тай тулгана   
   'CCCCCCCCCCCCCCC\n'    <--- 16  (Блок 6)
   'My agent identif'     <--- 16  (Блок 7)
   'ying code is:  p'     <--- 16  (Блок 8)    <--- Блок 8-д флагийн эхний тэмдэгт байгаа
   'icoCTF{ABCDEFG}.'     <--- 16  (Блок 9)    <--- мэдэгдэхгүй блок
   'Down with the So'     <--- 16  (Блок 10)   <--- мэдэгдэхгүй блок
```

* [python-3 скрипт](https://github.com/ByamB4/Capture-The-Flag/blob/master/Cryptography/src/block-cipher/aes-ecb/solve.py)
	
Fractionated Morse Cipher
Sebald cipher.
