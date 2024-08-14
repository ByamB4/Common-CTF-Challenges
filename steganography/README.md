## Text

- `White space`

  - `stegsnow -C -p <password> secret.txt`
  - [`stegcracker`](https://github.com/0xHasanM/SnowCracker) cracks snow password

- [`Binary character shape`](https://www.dcode.fr/binary-character-shape)

  - Example
    ```
    OI8I8o%o80bI8oO1bOPIbpIqodpIO81%PoOqIq/|\q1%1OdIqbP08\08dO|/88o||oq%IbqO8ddIddII81IO//OI88Ib8opIIp8oqpd%\pqbI|/bI
    ```

- [`Steg with base64`](https://github.com/hecky/stegb64)

  - Example
    ```
    PigngTnTtqWjrEFGdsSlrfQexoKfOhYyXkmkmxlq=
    ```

- [`Twitter secret messages`](https://holloway.nz/steg/)

  - Example
    ```
    i haｄ a grｅａｔ daｙ at the ｂeaｃh! #sunshｉne             
    ```

- `Zero width stegnography`

  - [online-tool](https://330k.github.io/misc_tools/unicode_steganography.html)
  - [python-tool](https://github.com/enodari/zwsp-steg-py)

  - **Example**
    ```
    &#8203;&#8203;&#8203;&#8203;&lrm;&rlm;&lrm;&#8203;&#8203;&#8203;&#8203;&zwnj;&zwj;&rlm;&#8203;
    &#8203;&#8203;&#8203;&lrm;&zwj;&rlm;&#8203;&#8203;&#8203;&#8203;&lrm;&zwj;&zwj;&#8203;&#8203;&#8203;
    &#8203;&rlm;&rlm;&#8203;&#8203;&#8203;&#8203;&#8203;&rlm;&lrm;&zwnj;&#8203;&#8203;&#8203;&#8203;&lrm;
    &#8203;&zwj;&#8203;&#8203;&#8203;&#8203;&zwj;&rlm;&zwj;&#8203;&#8203;&#8203;&#8203;&lrm;&#8203;&lrm;&#8203;
    &#8203;&#8203;&#8203;&zwnj;&rlm;&lrm;&#8203;&#8203;&#8203;&#8203;&lrm;&zwj;&lrm;&#8203;&#8203;&#8203;
    ```

## Image

- [`aperisolve`](https://www.aperisolve.com/) all in one tool

- `steghide` program that is able to hide data in various kinds of image and audio-files

  - `steghide extract -sf <filename>`

- [`stegseek`](https://github.com/RickdeJager/stegseek) fastest steghide password cracker

  - `stegseek <filename> rockyou.txt`

- [`zsteg`](https://github.com/zed-0xff/zsteg) use against least significant bit data in png and bmp

  - `zsteg -a <filename>`

- [`jsteg`](https://github.com/lukechampine/jsteg) another least significant bit tool extract data from jpg

  - `jsteg reveal <in.jpg> <output>`

- [`Slow Scan Television`](https://en.wikipedia.org/wiki/Slow-scan_television) send static image using only sound .wav

  - [writeup](https://ctftime.org/writeup/22354)

- `FFT`

  - [http://bigwww.epfl.ch/demo/ip/demos/FFT/](http://bigwww.epfl.ch/demo/ip/demos/FFT/)

- [`Least Significant Bit`](https://en.wikipedia.org/wiki/Bit_numbering#Least_significant_bit_in_digital_steganography)

  - [https://stylesuxx.github.io/steganography/](https://stylesuxx.github.io/steganography/)
  - `stegify -op decode -carrier cute_kittens.jpg -result hello`

- [`Steg for windows`](https://download.cnet.com/Steg/3000-2092_4-77792892.html)

  - http://diit.sourceforge.net/ Digital Invisible Ink Toolkit

- `Powershell`

  - [writeup](https://github.com/HHousen/PicoCTF-2021/blob/master/Forensics/Very%20very%20very%20Hidden/README.md)

- [`npiet`](https://www.bertnase.de/npiet/npiet-execute.php) execute program and shows result.

  - Example preview

    ![npiet-hello.gif](https://github.com/ByamB4/Common-CTF-Challenges/blob/main/Steganography/static/img/npiet_hello.gif)

## Audio

- [Audacity](https://www.audacityteam.org/) upload your file then view spectogram data

- [Sonic Visualizer](https://www.sonicvisualiser.org/) upload your file then view spectogram data

- [LSB](https://github.com/sniperline047/Audio-Steganography)

- [deepsound.exe](https://github.com/oneplus-x/DeepSound-2.0) is a steganography tool and audio converter that hides secret data into audio files.

## TODO

- stegoveritas
