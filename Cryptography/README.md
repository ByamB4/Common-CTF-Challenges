Encoding decoding
-----------------------

* `Base64` 
	
	Зарим тохиолдолд эвдэрсэн байдаг 
	
	* https://base64.guru/tools/repair
	
Transposition cipher
-----------------------

* `Rail Fence`

	Заримдаа zipzag cipher ч гэж нэрлэдэг. Тухайн plaintext ийг дээшээ доошоо мөр болгож дараан нэг мөрөөр нь нэгтгэж ciphertext үүсгэнэ. Дээшээ доошоо мөр болгож байгааг нь **key** гэж нэрлэнэ.
```
key        = 3
plaintext  = THISIS_SECRET
ciphertext = TIETHSSSCEI_R
T       I       E       T
  H   S   S   S   C   E
    I       _       R 
```
	
Substitution cipher
-----------------------

* `Vigenère cipher`

	Тухайн нэг түлхүүрээр нууцлах ба ерөнхийдөө тухайн plaintext key тэйгээ тааруулаад доорх хүснэгт ашиглаад ciphertext үүсгэнэ.
![https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/Images/Substitution%20cipher/Vigenere%20cipher.png](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/Images/Substitution%20cipher/Vigenere%20cipher.png)
``
key        = LEMONLEMONLE
plaintext  = ATTACKATDAWN
ciphertext = LXFOPVEFRNHR
Энд түлхүүр нь LEMON бөгөөд plaintext ийнхээ уртад тааруулан давтагдаж байна. 
Хүснэгтэнд A L тэмдэгтийн огтлолцол L учир ciphertext ийн эхний тэмдэгт нь L болж байгаа юм.
``
	
	
Asymmetric cryptography 
-----------------------

* `Rivest-Shamir–Adleman`

	* **n**-ийн хуваагдагчид буюу **p**, **q** хувьсагчийн утгийг олох.
		* [FactorDB](http://factordb.com/)
		* [IntegerECM](https://www.alpertron.com.ar/ECM.HTM)
	* **e** хэтэрхий том буюу (e < 65537) нөхцлийг хангаж байвал **wiener-attack** хэрэгжүүлж болно.
	* [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)
	* [Python2 - code](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/RSA/python2.py)
	* [Python3 - code](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/RSA/python3.py)
	* [Brute force - encrypt 4 letter](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/RSA/brute-force-encrypt-4-letter.py)
	* [Brute force - encrypt e guessing](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/RSA/find_e_python-2.py)
	* [`c1`, `c2`, `e1`, `e2` given](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/RSA/common_modules_attack.py) 
	* [`p`, `q`, `e` өгөгдсөн үед `d` олох](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/RSA/p_q_e_given-calculate-d.py)
	
	Public key, Private key, Encrypted text base64-өөр өгөгдсөн үед дараах байдлаар бодож болно
	* `base64 -d < pub.b64 > pub.der`
	* `base64 -d priv.b64 | openssl rsa -inform DER > out.key`
	* `base64 -d enc.b64 > enc`
	* `openssl rsautl -decrypt -inkey out.key < enc > decrypted`

Hash functions 
-----------------------

Hash нь ямар нэгэн мэдээллийн бүрэн бүтэн байдал, эх файл мөн эсэхийг шалгахад ихэвчлэ ашиглана. Дотроо хэд хэдэн тусдаа алгоритм байх бөгөөд хоорондоо битийн урт, бодож байгаа алгоритмаараа ялгаатай байна. Hash нь нэг зүгт нууцлалт бөгөөд эргүүлж задлана гэсэн ойлголт байхгүй, боломжит ганц арга нь **brute-force** билээ.

* `Message-Digest algorithm also MD5`
	128 бит урттай бөгөөд 16 байт гэсэн үг. Ингэснээр 32 ийн урттай hex утга гаргаж авна. 
	* `9e107d9d372bb6826bd81d3542a419d6`
	* [https://crackstation.net/](https://crackstation.net/)

	
Block cipher 
-----------------------

* `AES-ECB`
	
	ECB буюу Electronic Codebook нь plaintext-ийг тэнцүү урттай хэд хэдэн блок болгон хувааж нэг ижил түлхүүрээр нууцладаг. 
	
	![AES-Electronic codebook encryption image](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/Images/Block%20cipher/AES-ECB-encryption.png)
	
	Буцааж задлахдаа яг ижил зарчмаар задлана. 
	
	![AES-Electronic codebook decryption image](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/Images/Block%20cipher/AES-ECB-decyption.png)
	
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

* [python-3 скрипт](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/Code/Block-cipher/AES-ECB-decode.py)
	
