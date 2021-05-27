## Networking

- [`.pcapng`](https://github.com/pcapng/pcapng)

  Ихэнх файл ийм байгаад байдаггүй гэхдээ хувиргах шаардлага гарвал

  - [http://pcapng.com/](http://pcapng.com/)

- [`tcpflow`][tcpflow]

  Командын мөрний түүл `.pcap` файлаас нуугдсан файл илрүүлнэ.

```
tcpflow -r my_file.pcap
ls -1t | head -5 # see the last 5 recently modified files
```

- `3D принтер` өгөгдөл

  Зарим `.pcap` файл дээр `usb` өгөгдөл баригдах бөгөөд эдгээрээс зарим нь принтерийнх байна. Энэ нь 3D принтерийн дата байх үед түүнийг зурах `python` код.

  - [python2](https://github.com/ByamB4/CaptureTheFlagTool/blob/master/Miscellaneous/Code/pcap_3d_printer_capture.py)

```
BAR 148, 239, 48, 2
BAR 196, 191, 2, 48
BAR 148, 191, 48, 2
BAR 68, 191, 48, 2
BAR 76, 151, 40, 2
BAR 76, 119, 2, 32
```

- `USB (mouse) draw flag`

  Ихэнх тохиолдолд USB трафикаар флаг зурах юм.

  - [source-writeup](https://blogs.tunelko.com/2017/02/05/bitsctf-tom-and-jerry-50-points/)

- `Hex packet`

  Энэ нь `.pcap` файлыг hex болгож нууцалсан байдаг.

  - [https://hpd.gasmi.net/](https://hpd.gasmi.net/)
  Энэ нь `.pcap` файлыг hex болгож нууцалсан байдаг.

  - [https://hpd.gasmi.net/](https://hpd.gasmi.net/)
