## UPX Packed

Sometime UPX packed binary can't decompressed back. So author is manually changed some byte or even sections.

- You can try to guess
- Missing library. Append kernel32.dll to actual binary. [code](https://github.com/ByamB4/CCC/blob/master/Reverse%20Engineering/exe/src/append-kernel32.py)

## Python code packed

Extract python code from binary

- [PyInstallerExtractor](https://github.com/extremecoders-re/pyinstxtractor) Python script to extract the contents of a PyInstaller generated Windows executable file.
