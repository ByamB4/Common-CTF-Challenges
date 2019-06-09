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

Alien language 

![alt text](https://theinfosphere.org/images/9/9b/AL1_Key-2.png)
