# Misc

Grab bag of handy tools for oddball CTF tasks.

## Quick wins
- Check for visual obfuscation (pixelation, QR distortion) with specialized tools.
- For audio/tones, use DTMF or spectrogram helpers.
- Keep keyboard layout references for substitution-style puzzles.

## Tools and references

- **Decode android pattern lock**

  - [DecodeAndroidGesture](https://github.com/jzyra/DecodeAndroidGesture)

- **Recover data from pixelized image**

  - [Depix](https://github.com/beurtschipper/Depix)
    - [writeup](https://github.com/K1nd4SUS/CTF-Writeups/tree/main/dCTF_2021/Behind%20the%20scenes)

- **Extract numbers from an audio recording of the dial tones**

  - [online-tool](https://unframework.github.io/dtmf-detect/#/)
  - [dtmf-decoder](https://github.com/ribt/dtmf-decoder)

- **Recover QR code**

  - [qrazybox](https://merri.cx/qrazybox/)

- **Keyboard layouts (workman, qwerty, dvorak, colemak)**

  - [https://awsm-tools.com/keyboard-layout](https://awsm-tools.com/keyboard-layout)
  - **Example**
    ```
    Fy, sflla-oflla, hppla-oflla, jpf assfluk' U'l a yflak
    Dyab U gpbba hp bp grb ub bywpfgy bp jpf U'l sf;rwyflak•
    Ukkpcabucr akh U'l lahr pt wfvvrw sp byab akjbyukg
    Jpf saj us wumpmyrbuk' ptt pt lr, akh ub'oo gofr bp jpf akh
    U'l hrcasbabukg, lpwr byak rcrw hrlpksbwabukg
    ```

- **G-code for CNC Machining**

  - [https://gcodetutor.com/cnc-program-simulator.html](https://gcodetutor.com/cnc-program-simulator.html)
  - **Example**
    ```
    G01 X319.6025 Y6.859274
    G01 X319.2251 Y6.816967
    G01 X318.8967 Y6.706747
    G01 X318.6183 Y6.531953
    G01 X318.3934 Y6.299265
    ```

- **Punch card**
  - [https://www.masswerk.at/keypunch/](https://www.masswerk.at/keypunch/)
  
- [`pastebin`](https://pastebin.com/)

  - Can save your note with password protected url looks like `LX2gkn81`

## Git

  - **Show full history**
    - `git log --patch --follow -- text.txt > full_history.txt`
   
## LaTeX
  - **Read file**
    ```
    \renewcommand\r{\ifeof\file\else\read\file to\line\line\r\fi}
    \catcode`_=3
    \newread\file
    \openin\file=/etc/passwd
    \r
    \closein\file
    ```

  - **Extract all files**
    - [https://github.com/internetwache/GitTools/tree/master/Extractor](https://github.com/internetwache/GitTools/tree/master/Extractor)
   
  - **Symbols**
    - [https://detexify.kirelabs.org/symbols.html](https://detexify.kirelabs.org/symbols.html)
    - [https://snip.mathpix.com/](https://snip.mathpix.com/)
