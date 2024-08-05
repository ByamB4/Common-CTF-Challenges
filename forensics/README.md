## Windows

- Windows log file `.evtx`

  - Analyze using [`chainsaw`](https://github.com/WithSecureLabs/chainsaw)

- Registry `MS Windows registry file, NT/2000 or above`

  - Viewer [`registry-spy`](https://github.com/andyjsmith/Registry-Spy)

- RDP Bitmap Cache

  - [`bmc-tools`](https://github.com/ANSSI-FR/bmc-tools)
 
- Windows Management Instrumentation (WMI)

  - [`WMI Forensics`](https://github.com/davidpany/WMI_Forensics)    

## Image File

- `Magic numbers`

  - Fix magics [png-parser](https://github.com/ByamB4/Capture-The-Flag/blob/master/Forensics/src/png_parser.py)

- `pngcheck`

  - Command line tool, checks given png file corrupted or not.

- `2 same image`

  - We can use SUB, MUL, ... `compare 00000000.png 00000725.png -compose src diff.png`
 
- `aperisolve`[https://www.aperisolve.com/]

- `stegseek`[https://github.com/RickdeJager/stegseek]
  
  - `stegseek [IMAGE].jpg rockyou.txt`

## Browser related

- [`firefox_decrypt`](https://github.com/unode/firefox_decrypt)

  - Firefox Decrypt is a tool to extract passwords from Mozilla (Firefox™, Waterfox™, Thunderbird®, SeaMonkey®) profiles
   
## Wav File

- `SSTV`

  - [writeup](https://github.com/Dvd848/CTFs/blob/master/2019_picoCTF/m00nwalk.md)
  - [tutorial](https://ourcodeworld.com/articles/read/956/how-to-convert-decode-a-slow-scan-television-transmissions-sstv-audio-file-to-images-using-qsstv-in-ubuntu-18-04)

## PDF File

- `pdfinfo`

  - Command line tool to analyse given pdf.

- [`pdfminer`](https://github.com/euske/pdfminer)

  - `pdf2txt.py [INPUT].pdf`

- [`pdf-repair`](https://www.pdf-online.com/osa/repair.aspx)

  - Online tool to fix given pdf file.

- [`peepdf`](https://github.com/jesparza/peepdf)

  - Use case [`writeup`](https://saransappa.wordpress.com/2020/06/08/sec-t-ctf-2019-forensics-challenge-writeup/)

- **Extract**
  - [`pdfextract`](https://github.com/CrossRef/pdfextract)
  - `polyfile --html voip.html [FILENAME].pdf`

## Archive File

- Crack password protected zip file

  - Using [`fcrackzip`](https://www.geeksforgeeks.org/fcrackzip-tool-crack-a-zip-file-password-in-kali-linux/)
    - `fcrackzip -v -u -D -p rockyou.txt <filename.zip>`
  - Using [`zip2john`](https://github.com/openwall/john/blob/bleeding-jumbo/src/zip2john.c)

    - `zip2john <filename.zip> > hash.txt`
    - `john -w=rockyou.txt hash.txt`
    - `john --show hash.txt`

  - Edit hex byte to get some file for `zip`
    - `50 4B 03 04 14 00 09 00` to `50 4B 03 04 14 00 00 00`

## Document

- `olevba` detect VBA Macros, extract their source code in clear text.

## GIF File Forensics

- `Split images`

  - `convert test.gif %02d.png`
  - `ls *.png | while read filename; do convert $filename -transparent white $filename; done`
  - `ls *.png | while read filename; do convert $filename 00.png -gravity center -composite 00.png; done`


## Disk File

- `.img`

  - `fls`
    - `fls [FILE].img`
    - `fls [FILE].img [UID]`
    - `icat [FILE].img [UID]`
  
  - [DiskInternals Raid Recovery](https://www.diskinternals.com/raid-recovery/)

- `DOS/MBR boot sector`

  - `mmls dds2-alpine.flag.img`
  - `fls -o 0000002048 dds2-alpine.flag.img`
  - `fls -o 0000002048 dds2-alpine.flag.img 18290`
  - `icat -o 0000002048 dds2-alpine.flag.img 18291`
 
  - `qemu-system-x86_64 [IMAGE].img`

- `.iso`

  - LUKS encrypted file, we have to find password to extract.
  - `sudo cryptsetup open --type luks glaf.iso out_iso`
  - `sudo mount /dev/mapper/out_iso /mnt`

## Volatility 2

  - **Get imageinfo of given file**

    - `volatility -f [FILENAME] imageinfo`
  
  - **Showing windows info**

    - `volatility -f [FILENAME] windows.info`

  - **Show currently running process**

    - `volatility -f [FILENAME] --profile=[PROFILE] pslist`

  - **Dumping currently running process by PID**

    - `volatility -f [FILENAME] --profile=[PROFILE] procdump -p [PID] -D dump/`

  - **Locate the virtual addresses of registry hives in memory**

    - `volatility -f [FILENAME] --profile=[PROFILE] hivelist`
    - `volatility -f [FILENAME] --profile=[PROFILE] lsadump`
    - `volatility -f [FILENAME] --profile=[PROFILE] hashdump`
    - `volatility -f [FILENAME] --profile=[PROFILE] netscan`
    - `volatility -f [FILENAME] --profile=[PROFILE] shellbags`
    - `volatility -f [FILENAME] --profile=[PROFILE] clipboard`
    - `volatility -f [FILENAME] --profile=[PROFILE] pstree`
    - `volatility -f [FILENAME] --profile=[PROFILE] filescan`
    - `volatility -f [FILENAME] --profile=[PROFILE] consoles`

  - **Extract file from filescan output**

    - `volatility -f [FILENAME] --profile=[PROFILE] dumpfiles -Q [OFFSET] -D .`

  - **Extract and decrypt cached domain credentials stored in the registry**

    - `volatility -f [FILENAME] --profile=[PROFILE] hashdump -y [ADDRESS-OF-REGISTER-SYSTEM] -s [ADDRESS-OF-SYSTEMROOT-SAM]`


  - **Build custom profile (linux)**

    ```sh
    zip profile.zip module.dwarf System.map-4.15.0-213-generic
    cp volatility/volatility/plugins/overlays/linux/profile.zip
    ```

  - **Get dump profile name (linux)**

    - `python2 vol.py -f dump.mem --info`

  - **Show supported plugin commands (linux)**

    - `python2 vol.py -f dump.mem --profile=Linuxubuntux64 --help`

  - **Enumerate files (linux)**

    - `python2 vol.py -f dump.mem --profile=Linuxubuntux64 linux_enumerate_files`
   
  - **Recover file (linux)**
    - Get inode of the file
      - `python2 vol.py -f dump.mem --profile=Linuxubuntux64 linux_find_file -F /home/zangi/zan/needed.java`

    - **Recover file using inode**
      - `python2 vol.py -f dump.mem --profile=Linuxubuntux64 linux_find_file -i 0xffff95d2b7d2b890 -O out`
      
## Volatility 3

  - **Dump file**

    - `vol.py -f [FILENAME] -o [/path/to/dir] windows.dumpfiles`
    - `vol.py -f [FILENAME] -o [/path/to/dir] windows.dumpfiles ‑‑virtaddr [OFFSET]`
    - `vol.py -f [FILENAME] -o [/path/to/dir] windows.dumpfiles ‑‑physaddr [OFFSET]`
