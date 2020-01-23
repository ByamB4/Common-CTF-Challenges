Cryptography
-----------------------

Encoding decoding
-----------------------

* `Base64` 
	
	Зарим тохиолдолд эвдэрсэн байдаг 
	
	* https://base64.guru/tools/repair
	
	
Asymmetric cryptography 
-----------------------

* [`RSA`](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

	Ихэнх тохиолдолд `n`, `c`, `e` өгөгдөх бөгөөд эхлээд [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool) ашиглаж үзэх хэрэгтэй. Бусад тохиолдолд гараар бодно.
	* [FactorDB](http://factordb.com/)
	* [IntegerECM](https://www.alpertron.com.ar/ECM.HTM)
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

Block cipher 
-----------------------

* `AES-ECB`
	
	ECB буюу Electronic Codebook нь plaintext-ийг тэнцүү урттай хэд хэдэн блок болгон хувааж нэг ижил түлхүүрээр нууцладаг. 
	
	![AES-Electronic codebook encryption image](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/Images/Block%20cipher/AES-ECB-encryption.png)
	
	Буцааж задлахдаа яг ижил зарчмаар задлана. 
	
	![AES-Electronic codebook decryption image](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/Images/Block%20cipher/AES-ECB-decyption.png)
	
	Тэгэхээр бид түлхүүрийг олохоос илүү аль нэг блок дээр байгаа текстийг нэг унших нь илүү үр дүнтэй юм. 

```
   'Agent,\nGreetings' <--- 16  (Блок 1)
   '. My situation r'  <--- 16  (Блок 2)
   'eport is as foll'  <--- 16  (Блок 3)
   'ows:\nAAAAAAAAAAA' <--- 16  (Блок 4) <--- Оролт эхлэх хэсэг 
   'BBBBBBBBBBBBBBBB'  <--- 16  (Блок 5) <--- padding 
   'CCCCCCCCCCCCCCCC'  <--- 16  (Блок 6) 
   '\nMy agent identi' <--- 16  (Блок 7)
   'fying code is:  '  <--- 16  (Блок 8)  <---мэдэгдэж буй блок
   'flagCTF{ABCDEFG}'  <--- 16  (Блок 9)  <---бидний бай _(ABCDEFG нь гүйцээж байгаа)_
   '.Down with the S'  <--- 16  (Блок 10) <---мэдэгдэж буй блок
```

Бид эндээс Блок 6 ийн нэг тэмдэгтийг хасвал манай флагийн нэг тэмдэгт дээшээ гарч ирнэ. 


```
   'Agent,\nGreetings'    <--- 16  (Block 1)
   '. My situation r'     <--- 16  (Block 2)
   'eport is as foll'     <--- 16  (Block 3)
   'ows:\nAAAAAAAAAAA'    <--- 16  (Block 4)
   'ying code is:  %s'    <--- 16  (Block 5)    <--- replace %s to char in range(32,128)   
   'CCCCCCCCCCCCCCC\n'    <--- 16  (Block 6)
   'My agent identif'     <--- 16  (Block 7)
   'ying code is:  p'     <--- 16  (Block 8)    <--- Now we know block 8 has our one byte flag
   'icoCTF{ABCDEFG}.'     <--- 16  (Block 9)    <--- unknown block 
   'Down with the So'     <--- 16  (Block 10)   <---known Block
```
	

	
