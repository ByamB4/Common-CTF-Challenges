# Forensics

Disk, memory, network, and artifact triage tips for CTFs.

## Quick wins
- Run `strings`/`xxd` early; many flags hide in plain sight.
- For images, try `steghide`/`stegseek`, metadata checks, and pixel diffs before heavier analysis.
- On memory dumps, identify the profile first (`imageinfo`/`linux_banner`), then dump interesting processes/files.
- Convert PCAPs to focused outputs (DNS queries, HTTP files, USB keystrokes) instead of manual clicking.

## Disk images
- EnCase/EWF: inspect with Autopsy (GUI).
- Raw `.img`:
  - List: `fls file.img`
  - File by inode: `icat file.img <inode>`
- DOS/MBR offset example:
  ```
  mmls dds2-alpine.flag.img
  fls -o 0000002048 dds2-alpine.flag.img
  icat -o 0000002048 dds2-alpine.flag.img 18291
  ```
- Boot/run: `qemu-system-x86_64 image.img`
- ISO (LUKS): `sudo cryptsetup open --type luks glaf.iso out_iso && sudo mount /dev/mapper/out_iso /mnt`
- Quick scan: `xxd image | grep "F.L.A" -B 10 -A 10`

## Memory analysis (Volatility 2)
- Find profile: `volatility -f file.mem imageinfo`
- Windows highlights:
  - `pslist`, `pstree`, `netscan`, `hashdump`, `lsadump`, `cmdscan`, `envars`
  - Dump process: `volatility -f file.mem --profile=PROFILE procdump -p PID -D dump/`
  - File recovery: `filescan` -> `dumpfiles -Q OFFSET -D .`
  - Cached credentials: `hivelist` -> `hashdump -y <system> -s <sam>`
- Interesting artifacts: `\Google\Chrome\User Data\Default\History`
- Linux highlights:
  - Version peek: `strings file.mem | grep "Linux version"`
  - Build custom profile if missing (module.dwarf + System.map -> zip profile.zip)
  - Commands: `linux_bash`, `linux_pstree`, `linux_psaux`, `linux_malfind`, `linux_enumerate_files`, `linux_volshell`
  - Recover file:
    ```
    volatility -f file.mem --profile=PROFILE linux_find_file -F /home/ctf/flag.txt
    volatility -f file.mem --profile=PROFILE linux_find_file -i <inode> -O out
    ```

## Memory analysis (Volatility 3)
- Dump file: `volatility3 -f file.mem -o out/ windows.dumpfiles`
- With address: `volatility3 -f file.mem -o out/ windows.dumpfiles --virtaddr OFFSET`

## PCAPs and traffic
- TCP flow reassembly: `tcpflow -r capture.pcap`
- DNS extraction helper: `forensics/src/pcap_extract_dns_query.py`
- USB keyboard parsers:
  - https://github.com/5h4rrk/CTF-Usb_Keyboard_Parser
  - https://github.com/TeamRocketIst/ctf-usb-keyboard-parser
- USB mouse drawing reference: https://blogs.tunelko.com/2017/02/05/bitsctf-tom-and-jerry-50-points/
- 3D printer G-code examples (look for repeated `BAR` lines)

## Windows artifacts
- Event logs `.evtx`: analyze with Chainsaw (https://github.com/WithSecureLabs/chainsaw)
- Registry hives: Registry-Spy (https://github.com/andyjsmith/Registry-Spy)
- RDP Bitmap Cache: https://github.com/ANSSI-FR/bmc-tools
- WMI artifacts: https://github.com/davidpany/WMI_Forensics

## Images
- Quick sites/tools: https://www.aperisolve.com/, https://github.com/RickdeJager/stegseek, https://github.com/lukechampine/jsteg
- Sample commands:
  - `stegseek image.jpg rockyou.txt`
  - Compare two images: `compare 00000000.png 00000725.png -compose src diff.png`
- PNG helpers: https://github.com/sherlly/PCRT, `forensics/src/png_parser.py`, https://github.com/Ge0rg3/ctf-png-size-solver
- Hide data in image height: https://cyberhacktics.com/hiding-information-by-changing-an-images-height/

## Browsers
- Decrypt Firefox credentials: https://github.com/unode/firefox_decrypt

## Audio / WAV
- SSTV reference writeup: https://github.com/Dvd848/CTFs/blob/master/2019_picoCTF/m00nwalk.md
