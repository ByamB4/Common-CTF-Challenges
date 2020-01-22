Steganography
-----------------------

* [`Stegsolve.jar`](https://github.com/zardus/ctf-tools/blob/master/stegsolve/install)

	Ихэнх даалгавар дээр ашиглаж болох бөгөөд өнгө бүр дээр хувирлыг харуулна.

* `Offset`
	Stegsolve-оор offset ээр нь гүйлгэнэ.

![Offset image](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Steganography/img/frame_031_delay-0.07s.png)

* [`steghide`](http://steghide.sourceforge.net/download.php)

	Нууц үгээр тухайн зурагтаа файл нуух, гаргаж авах түүл. PNG болон BMP зурагтай л ажиллаж чадна.
	
* [zsteg](https://github.com/zed-0xff/zsteg)
	
	Энэ түүл нь PNG болон BMP файл дотор нуугдсан өгөгдлийг илрүүлнэ.

* [`Least Significant Bit`](https://en.wikipedia.org/wiki/Bit_numbering#Least_significant_bit_in_digital_steganography) 

	Layer дээр өгөгдөл нуугдаагүй битэн дотор нуугдсан гэсэн үг. Тиймээс `Stegsolve.jar` аар Data Extract гээд үзээд явна. Эсвэл онлайн түүлээр шалгана.
	* [https://stylesuxx.github.io/steganography/](https://stylesuxx.github.io/steganography/)
	* `stegify -op decode -carrier cute_kittens.jpg -result hello`

* [`Steg with base64`](https://github.com/bzorigt/stegb64)

	Шинэ төрлийн base64 гэж хэлж болно. Энгийн base64 тайлахгүй бөгөөд одоогийн байдлаар доорх код л тайлна.
	* [python2](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Steganography/code/stegb64.py)

* [`White space steganography`] 

	Хоосон зай, таб зэрэгт нуугдсан мессеж байна. `stegsnow` ашиглаж тайлна. Гэхдээ энд заавал нууц үг хэрэгтэй бөгөөд хэрэв нууц үгтэй бол дараах командыг дагуу тайлна.
	* `stegsnow -C -p password secret.txt`
