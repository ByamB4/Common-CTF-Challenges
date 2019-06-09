Тугийг олзлох түүлүүд
===============

> С. Бямбадалай | 06-08-2019
--------------------------
Live тэмцээний үед түүл хайж цаг алдахын оронд өөрийн бэлдсэн түүл, код зэргийг өөр өөртөө бэлдсэн болно. 

Татах линк 
------------------
* Burp suite Pro -> [https://drive.google.com/open?id=10RwrjnC4diW3nlGS0SBRpkR05L93zDOE](https://drive.google.com/open?id=10RwrjnC4diW3nlGS0SBRpkR05L93zDOE)
* IDA PRO        -> [https://drive.google.com/open?id=1alqfGr6w9RBoRWqMo_7GEvLhu8H8lkuc](https://drive.google.com/open?id=1alqfGr6w9RBoRWqMo_7GEvLhu8H8lkuc)
* StegSolve.jar  -> [https://drive.google.com/open?id=1VFn2ukSjw7YU8PeJNdR4KwndWBR1ejEY](https://drive.google.com/open?id=1VFn2ukSjw7YU8PeJNdR4KwndWBR1ejEY)

Esoteric Languages
-----------------------

* Esoteric төрлийн ихэнх хэлнүүдийг ажиллуулах сайт. [https://tio.run/](https://tio.run/)

  
* Brainfuck
  	8 тэмдэгтийг ашиглаж декод хийнэ. [https://www.dcode.fr/brainfuck-language](https://www.dcode.fr/brainfuck-language)
 ```
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>+++++++++++++++++.--.--------------.+++++++++++++.----.-----------
--.++++++++++++.--------.<------------.<++.>>----.+.<+++++++++++.+++++++++++++.>+++++++++++++++++.-------------
--.++++.+++++++++++++++.<<.>>-------.<+++++++++++++++.>+++..++++.--------.+++.<+++.<++++++++++++++++++++++++++
.<++++++++++++++++++++++.>++++++++++++++..>+.----.>------.+++++++.--------.<+++.>++++++++++++..-------.++.
```
  
* JS-Fuck
	6 тэмдэгтийг ашиглаж декод хийнэ. [https://enkhee-osiris.github.io/Decoder-JSFuck/](https://enkhee-osiris.github.io/Decoder-JSFuck/)
```
[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!
```

* Cow
	3 тэмдэгтийг ашиглаж декод хийнэ. 
```
MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO
 MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO
 MoO MoO Moo MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO Moo MoO MoO
 MoO MoO MoO MoO MoO Moo Moo MoO MoO MoO Moo OOO MoO MoO MoO MoO
 ```

Steganography
-----------------------

* [Stegsolve.jar](https://github.com/zardus/ctf-tools/blob/master/stegsolve/install)

	Ихэнх даалгавар дээр ашиглаж болох бөгөөд өнгө бүр дээр хувирлыг харуулна.
	
* [steghide](http://steghide.sourceforge.net/download.php)

	Нууц үгээр тухайн зурагтаа файл нуух, гаргаж авах түүл. PNG болон BMP зурагтай л ажиллаж чадна.
	
* [zsteg](https://github.com/zed-0xff/zsteg)
	
	Энэ түүл нь PNG болон BMP файл дотор нуугдсан өгөгдлийг илрүүлнэ.

* [Least Significant Bit](https://en.wikipedia.org/wiki/Bit_numbering#Least_significant_bit_in_digital_steganography) 

	Зурган доторх битүүдийг хөндлөнгөөр ашиглан өгөгдөл нуух. 
	* [https://stylesuxx.github.io/steganography/](https://stylesuxx.github.io/steganography/)
	

Cryptography
-----------------------

* Ихэнх төрлийн transposition cipher дээр ашиглаж болох онлайн түүл. 
	* [https://quipqiup.com/](https://quipqiup.com/)
	* [https://gchq.github.io/CyberChef/](https://gchq.github.io/CyberChef/)

* Ceaser - 26

	Англи хэлний 26 үсгэн дотор шилжилт хийж текстээ нууцалж задлана. Rot гэдэг нь хэдэн шилжилт хийснийг илэрхийлнэ. Маш олон онлайн түүл байгаа. Гэвч коммандны мөрнөөс хийвэл илүү амар `caesar` ашиглан (`apt install bsdgames`) аас суулгана. 
	
	```cipher='jeoi{geiwev_gmtliv_ws_svmkmrep}' ; for i in {0..25}; do echo $cipher | caesar $i; done```
	
	* [https://www.dcode.fr/caesar-cipher](https://www.dcode.fr/caesar-cipher)
	* [https://cryptii.com/pipes/caesar-cipher](https://cryptii.com/pipes/caesar-cipher)
	* [https://rot13.com/](https://rot13.com/)
``` 
Svylt Pwzbt pz zptwsf kbttf alea vm aol wypuapun huk afwlzlaapun pukbzayf. Svylt Pwzbt ohz illu aol pukbzayf'z zahukhyk kbttf alea lcly zpujl aol 1500z, dolu hu buruvdu wypualy avvr h nhsslf vm afwl huk zjyhtislk pa av thrl h afwl zwljptlu ivvr. Pa ohz zbycpclk uva vusf mpcl jluabyplz, iba hszv aol slhw puav lsljayvupj afwlzlaapun, ylthpupun lzzluaphssf bujohunlk. Pa dhz wvwbshypzlk pu aol 1960z dpao aol ylslhzl vm Slayhzla zollaz jvuahpupun Svylt Pwzbt whzzhnlz, huk tvyl yljluasf dpao klzravw wbispzopun zvmadhyl sprl Hskbz WhnlThrly pujsbkpun clyzpvuz vm Svylt Pwzbt.
```
	
* Keyboard шилжилт

	Keyboard дахь үсэгнүүдийг баруун тийш нь шилжүүлж нууцална.
	* [https://www.dcode.fr/keyboard-shift-cipher](https://www.dcode.fr/keyboard-shift-cipher)
``` 
:ptr, O[di, od do,[;u fi,,u yrcy pg yjr [tomyomh smf yu[rdryyomh omfidytu/ :ptr, O[di, jsd nrrm yjr omfidytu\d dysmfstf fi,,u yrcy rbrt domvr yjr 26--d. ejrm sm imlmpem [tomyrt yppl s hs;;ru pg yu[r smf dvts,n;rf oy yp ,slr s yu[r d[rvo,rm nppl/ Oy jsd ditbobrf mpy pm;u gobr vrmyitord. niy s;dp yjr ;rs[ omyp r;rvytpmov yu[rdryyomh. tr,somomh rddrmyos;;u imvjsmhrf/ Oy esd [p[i;stodrf om yjr 207-d eoyj yjr tr;rsdr pg :rytsdry djrryd vpmysomomh :ptr, O[di, [sddshrd. smf ,ptr trvrmy;u eoyj frdlyp[ [in;odjomh dpgyestr ;olr S;fid {shr<slrt omv;ifomh brtdopmd pg :ptr, O[di,/
```

* XOR
	
	Бүх текст XOR үйлдэл хийх боломжтой `\xde\xad\xbe\xef` үүнийг өөрийн компьютер дотроо тайлна гэвэл `pwntools` ашиглаж болно.
```
 python >>> import pwn; pwn.xor("KEY", "RAW_BINARY_CIPHER")
 ```
 
 * [Atbash Cipher](https://en.wikipedia.org/wiki/Atbash)

	Mapping хийдэг cipher `A` үсгийг `Z` ээр солих гэх `B`-г `Y` солих гэх мэт.
	* [http://rumkin.com/tools/cipher/atbash.php](http://rumkin.com/tools/cipher/atbash.php)
	
* [Vigenere Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

	Түлхүүртэй байх бөгөөд тэр түлхүүрээрээ нууцалж буцааж задалж болно.
	* [https://www.guballa.de/vigenere-solver](https://www.guballa.de/vigenere-solver)
	* [https://www.dcode.fr/vigenere-cipher](https://www.dcode.fr/vigenere-cipher)
	* [https://f00l.de/hacking/vigenere.php](https://f00l.de/hacking/vigenere.php)
	
* [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

	Ихэнх тохиолдолд `n`, `c`, `e` өгөгдөх бөгөөд эхлээд [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool) ашиглаж үзэх хэрэгтэй. Бусад тохиолдолд гараар бодно.
	* [FactorDB](http://factordb.com/)
	* [IntegerECM](https://www.alpertron.com.ar/ECM.HTM)
	* [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)
	* [Python2 - code](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/RSA/python2.py)
	* [Python3 - code](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Cryptography/RSA/python3.py)
	
* Railfence Cipher
	
	Симметрик төрлийн түлхүүртэй доош дээшээ шилжинэ.
	* [http://rumkin.com/tools/cipher/railfence.php](http://rumkin.com/tools/cipher/railfence.php)
```
s     e
  e  r  t  => seertc 
    c 
```

Networking
---------------

* [Wireshark](https://www.wireshark.org/)

	`.pcap` файлууд дээр анализ хийнэ.

* [Network Miner](http://www.netresec.com/?page=NetworkMiner)

	`.pcap` болон `.pcapng` файлууд дээр анализ хийнэ.
	
* [`.pcapng`](https://github.com/pcapng/pcapng)

	Ихэнх файл ийм байгаад байдаггүй гэхдээ хувиргах шаардлага гарвал
	* [http://pcapng.com/](http://pcapng.com/)
	
* [`tcpflow`][tcpflow]

	Командын мөрний түүл `.pcap` файлаас нуугдсан файл илрүүлнэ. 
```
tcpflow -r my_file.pcap
ls -1t | head -5 # see the last 5 recently modified files
```


PHP
------------

* Magic Hashes
	
	Хуучин PHP дээр зарим хаш ижил утгатай байдаг `0e` ээр эхэлсэн байна. Үүнийг `==` оператор дээр ашиглаж болно.
	* [https://github.com/spaze/hashes](https://github.com/spaze/hashes)
| Plaintext | MD5 Hash |
| --------- | -------- |
|240610708|0e462097431906509019562988736854|
|QLTHNDT|0e405967825401955372549139051580|
|QNKCDZO|0e830400451993494058024219903391|
|PJNPDWY|0e291529052894702774557631701704|
|NWWKITQ|0e763082070976038347657360817689|
|NOOPCJF|0e818888003657176127862245791911|
|MMHUWUV|0e701732711630150438129209816536|
|MAUXXQC|0e478478466848439040434801845361|
|IHKFRNS|0e256160682445802696926137988570|
|GZECLQZ|0e537612333747236407713628225676|
|GGHMVOE|0e362766013028313274586933780773|
|GEGHBXL|0e248776895502908863709684713578|
|EEIZDOI|0e782601363539291779881938479162|
|DYAXWCA|0e424759758842488633464374063001|
|DQWRASX|0e742373665639232907775599582643|
|BRTKUJZ|00e57640477961333848717747276704|
|ABJIHVY|0e755264355178451322893275696586|
|aaaXXAYW|0e540853622400160407992788832284|
|aabg7XSs|0e087386482136013740957780965295|
|aabC9RqS|0e041022518165728065344349536299|

| Plaintext | SHA1 Hash |
| --------- | --------- |
|aaroZmOk|0e66507019969427134894567494305185566735|
|aaK1STfY|0e76658526655756207688271159624026011393|
|aaO8zKZF|0e89257456677279068558073954252716165668|
|aa3OFF9m|0e36977786278517984959260394024281014729|

| Plaintext | MD4 Hash |
| --------- | --------- |
|bhhkktQZ|0e949030067204812898914975918567|
|0e001233333333333334557778889|0e434041524824285414215559233446|
|0e00000111222333333666788888889|0e641853458593358523155449768529|
|0001235666666688888888888|0e832225036643258141969031181899|

	
