## Text

- [`Binary character shape`](https://www.dcode.fr/binary-character-shape)

```
OI8I8o%o80bI8oO1bOPIbpIqodpIO81%PoOqIq/|\q1%1OdIqbP08\08dO|/88o||oq%IbqO8ddIddII81IO//OI88Ib8opIIp8oqpd%\pqbI|/bI
```

## Image

- [`steghide`](http://steghide.sourceforge.net/download.php)

  - To extract files `steghide extract -sf <filename>`
  - To brute force password [`stegcracker`](https://github.com/Va5c0/Steghide-Brute-Force-Tool)

- [zsteg](https://github.com/zed-0xff/zsteg)

  Энэ түүл нь PNG болон BMP файл дотор нуугдсан өгөгдлийг илрүүлнэ.

- `jsteg`

  Хуучин түүл бөгөөд `.jpg` файлаас өгөгдөл гарган авна.

- `binary image`

  - [https://www.dcode.fr/binary-image](https://www.dcode.fr/binary-image)

- `FFT`

  - [http://bigwww.epfl.ch/demo/ip/demos/FFT/](http://bigwww.epfl.ch/demo/ip/demos/FFT/)

- [`Least Significant Bit`](https://en.wikipedia.org/wiki/Bit_numbering#Least_significant_bit_in_digital_steganography)

  Layer дээр өгөгдөл нуугдаагүй битэн дотор нуугдсан гэсэн үг. Тиймээс `Stegsolve.jar` аар Data Extract гээд үзээд явна. Эсвэл онлайн түүлээр шалгана.

  - [https://stylesuxx.github.io/steganography/](https://stylesuxx.github.io/steganography/)
  - `stegify -op decode -carrier cute_kittens.jpg -result hello`

- [`Steg with base64`](https://github.com/bzorigt/stegb64)

  Шинэ төрлийн base64 гэж хэлж болно. Энгийн base64 тайлахгүй бөгөөд одоогийн байдлаар доорх код л тайлна.

  - [python2](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Steganography/code/stegb64.py)

- [`White space steganography`]

  Хоосон зай, таб зэрэгт нуугдсан мессеж байна. `stegsnow` ашиглаж тайлна. Гэхдээ энд заавал нууц үг хэрэгтэй бөгөөд хэрэв нууц үгтэй бол дараах командыг дагуу тайлна.

  - `stegsnow -C -p password secret.txt`

## Audio

- LSB Steganography

  - [repo](https://github.com/sniperline047/Audio-Steganography)
