## Disk File

- `EWF/Expert Witness/EnCase`

  - [`Autospy`](https://www.autopsy.com/)

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
 
- Just use `strings`
  - `xxd image | grep "F.L.A" -B 10 -A 10`

## Volatility 2

  - **Interesting files**

    - `\Google\Chrome\User Data\Default\History`

  - **Get imageinfo of given file**

    - `volatility -f [FILENAME] imageinfo`
  
  - **Showing windows info**

    - `volatility -f [FILENAME] windows.info`

  - **Show currently running process**

    - `volatility -f [FILENAME] --profile=[PROFILE] pslist`

  - **Dumping currently running process by PID**

    - `volatility -f [FILENAME] --profile=[PROFILE] procdump -p [PID] -D dump/`

  - **Common commands**

    - `volatility -f [FILENAME] --profile=[PROFILE] lsadump`
    - `volatility -f [FILENAME] --profile=[PROFILE] hashdump`
    - `volatility -f [FILENAME] --profile=[PROFILE] netscan`
    - `volatility -f [FILENAME] --profile=[PROFILE] shellbags`
    - `volatility -f [FILENAME] --profile=[PROFILE] clipboard`
    - `volatility -f [FILENAME] --profile=[PROFILE] pstree`
    - `volatility -f [FILENAME] --profile=[PROFILE] filescan`
    - `volatility -f [FILENAME] --profile=[PROFILE] consoles`
    - `volatility -f [FILENAME] --profile=[PROFILE] cmdscan`

  - **Extract file from filescan output**

    - `volatility -f [FILENAME] --profile=[PROFILE] dumpfiles -Q [OFFSET] -D .`

  - **Extract and decrypt cached domain credentials stored in the registry**
    - `volatility -f [FILE] --profile=[PROFILE] hivelist`
    - `volatility -f [FILE] --profile=[PROFILE] hashdump -y [ADDRESS-OF-REGISTER-SYSTEM] -s [ADDRESS-OF-SYSTEMROOT-SAM]`

### Working with linux
  - **Get linux version**
    - `strings [FILE] | grep "Linux version"`
    
  - **Build custom profile (linux)**

    - **Method 1 (use docker slow but confident)**
      - [https://github.com/hanasuru/vol_profile_builder/blob/master/build.sh](https://github.com/hanasuru/vol_profile_builder/blob/master/build.sh)
      - `./build.sh 18.04 4.15.0-213-generic`

    - **Method 2 (custom profile)**
      ```sh
      zip profile.zip module.dwarf System.map-4.15.0-213-generic
      cp volatility/volatility/plugins/overlays/linux/profile.zip
      ```
      
  - **Show supported plugin commands**

    - `volatility -f [FILENAME] --profile=[PROFILE] --help`

  - **Enumerate files**

    - `volatility -f [FILENAME] --profile=[PROFILE] linux_enumerate_files`
   
  - **Recover file**
    - **Get inode of the file**
      - `volatility -f [FILENAME] --profile=[PROFILE] linux_find_file -F /home/ctf/flag.txt`

    - **Recover file using inode**
      - `volatility -f [FILENAME] --profile=[PROFILE] linux_find_file -i [INODE] -O out`
     
  - **Common commands**
    - `volatility -f [FILENAME] --profile=[PROFILE] linux_bash`
    - `volatility -f [FILENAME] --profile=[PROFILE] linux_bash_env`
    - `volatility -f [FILENAME] --profile=[PROFILE] linux_psaux`
    - `volatility -f [FILENAME] --profile=[PROFILE] linux_psenv`

## Volatility 3

  - **Dump file**

    - `volatility3 -f [FILENAME] -o [/path/to/dir] windows.dumpfiles`
    - `volatility3 -f [FILENAME] -o [/path/to/dir] windows.dumpfiles ‑‑virtaddr [OFFSET]`
    - `volatility3 -f [FILENAME] -o [/path/to/dir] windows.dumpfiles ‑‑physaddr [OFFSET]`

## PCAP file

- **USB traffic**
  - [CTF-Usb_Keyboard_Parser](https://github.com/5h4rrk/CTF-Usb_Keyboard_Parser)
  - [ctf-usb-keyboard-parser](https://github.com/TeamRocketIst/ctf-usb-keyboard-parser)

- **Extract DNS query**
  - [pcap_extract_dns_query.py](https://github.com/ByamB4/Common-CTF-Challenges/blob/main/forensics/src/pcap_extract_dns_query.py)
  
- `tcpflow -r [INPUT].pcap`

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

- [`Hide data in height`](https://cyberhacktics.com/hiding-information-by-changing-an-images-height/)

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
   
  - `bkcrack`

## Document

- `olevba` detect VBA Macros, extract their source code in clear text.

## GIF File Forensics

- `Split images`

  - `convert test.gif %02d.png`
  - `ls *.png | while read filename; do convert $filename -transparent white $filename; done`
  - `ls *.png | while read filename; do convert $filename 00.png -gravity center -composite 00.png; done`


### React native Hermes bytecode [hbc-tool](https://github.com/P1sec/hermes-dec)
  - `hbc-file-parser index.android.bundle > out.hasm`
  - `hbc-disassembler index.android.bundle out.dis`
  - `hbc-decompiler index.android.bundle out.js`


## Roblox

  - [show old version/source code](https://github.com/PuruSinghvi/CTF-Writeups/tree/main/SunshineCTF%202024/Forensics/Rogue%20Robloxians)
