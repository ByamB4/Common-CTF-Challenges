## General

- `Reversed hex file`

  - Using python `open('output2.txt', 'wb').write(open('output.txt', 'rb').read()[::-1])`.

- `Python bytecode`

  - You can use `uncompyle6` to decompile.

## PNG File

- `Magic numbers`

  - Fix magics [png-parser](https://github.com/ByamB4/Capture-The-Flag/blob/master/Forensics/src/png_parser.py)

- `pngcheck`

  - Command line tool, checks given png file corrupted or not.

- `2 same image`

  - We can use SUB, MUL, ... `compare 00000000.png 00000725.png -compose src diff.png`

## Archive File

- `nomarch`

  - `ARC` archive data
  
- `ppmd`
  
  - `PPMD` archive data

- `cabextract`

  - `Microsoft Cabinet` archive data
  
- `bunzip2`

  - `bzip2` compressed data
  
- `xz`

  - `XZ` compressed data

- `gzip`
  
  - `gzip` compressed data

- `tar`

  - `POSIX tar` archive (GNU)

- `kgb`

  - `KGB Archiver` file

- `rzip`

  - `rzip compressed` data

- `zoo`

  - `Zoo archive` data
  
## PDF File

- `pdfinfo`

  - Command line tool to analyse given pdf.

- [`pdfminer`](https://github.com/euske/pdfminer)

  - Lot of useful tools.

- `[pdf-repair](https://www.pdf-online.com/osa/repair.aspx)`

  - Online tool to fix given pdf file.

## GIF File Forensics

- `Split images`

  - `convert test.gif %02d.png`
  - `ls *.png | while read filename; do convert $filename -transparent white $filename; done`
  - `ls *.png | while read filename; do convert $filename 00.png -gravity center -composite 00.png; done`

## Disk File

- `.img`

  - [DiskInternals Raid Recovery](https://www.diskinternals.com/raid-recovery/)

- `.iso`

  - LUKS encrypted file, we have to find password to extract.
  - `sudo cryptsetup open --type luks glaf.iso out_iso`
  - `sudo mount /dev/mapper/out_iso /mnt`

- `Volatility`

  Show imageinfo on given file 
  - `volatility -f [FILENAME] imageinfo`
  
  Show currently running process
  - `volatility -f [FILENAME] --profile=[PROFILE] pslist`
  
  Dumping currently running process by PID
  - `volatility -f [FILENAME] --profile=[PROFILE] procdump -p [PID] -D dump/`
  
  Locate the virtual addresses of registry hives in memory
  - `volatility -f [FILENAME] --profile=[PROFILE] hivelist`
  
  Extract and decrypt cached domain credentials stored in the registry
  - `volatility -f [FILENAME] --profile=[PROFILE] hashdump -y [ADDRESS-OF-REGISTER-SYSTEM] -s [ADDRESS-OF-SYSTEMROOT-SAM]`
  
## General

- `Reversed hex file`

  - Using python `open('output2.txt', 'wb').write(open('output.txt', 'rb').read()[::-1])`.

- `Python bytecode`

  - You can use `uncompyle6` to decompile.

## PNG File

- `Magic numbers`

  - Fix magics [png-parser](https://github.com/ByamB4/Capture-The-Flag/blob/master/Forensics/src/png_parser.py)

- `pngcheck`

  - Command line tool, checks given png file corrupted or not.

- `2 same image`

  - We can use SUB, MUL, ... `compare 00000000.png 00000725.png -compose src diff.png`

## PDF File

- `pdfinfo`

  - Command line tool to analyse given pdf.

- [`pdfminer`](https://github.com/euske/pdfminer)

  - Lot of useful tools.

- `[pdf-repair](https://www.pdf-online.com/osa/repair.aspx)`

  - Online tool to fix given pdf file.

## GIF File Forensics

- `Split images`

  - `convert test.gif %02d.png`
  - `ls *.png | while read filename; do convert $filename -transparent white $filename; done`
  - `ls *.png | while read filename; do convert $filename 00.png -gravity center -composite 00.png; done`

## Disk File

- `.img`

  - [DiskInternals Raid Recovery](https://www.diskinternals.com/raid-recovery/)

- `.iso`

  - LUKS encrypted file, we have to find password to extract.
  - `sudo cryptsetup open --type luks glaf.iso out_iso`
  - `sudo mount /dev/mapper/out_iso /mnt`
