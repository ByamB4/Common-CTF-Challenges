## Zero width space

```
&#8203;&#8203;&#8203;&#8203;&lrm;&rlm;&lrm;&#8203;&#8203;&#8203;&#8203;&zwnj;&zwj;&rlm;&#8203;&#8203;&#8203;&#8203;&lrm;&zwj;&rlm;&#8203;&#8203;&#8203;&#8203;&lrm;&zwj;&zwj;&#8203;&#8203;&#8203;&#8203;&rlm;&rlm;&#8203;&#8203;&#8203;&#8203;&#8203;&rlm;&lrm;&zwnj;&#8203;&#8203;&#8203;&#8203;&lrm;&#8203;&zwj;&#8203;&#8203;&#8203;&#8203;&zwj;&rlm;&zwj;&#8203;&#8203;&#8203;&#8203;&lrm;&#8203;&lrm;&#8203;&#8203;&#8203;&#8203;&zwnj;&rlm;&lrm;&#8203;&#8203;&#8203;&#8203;&lrm;&zwj;&lrm;&#8203;&#8203;&#8203;
```

```python
import requests as req
import zwsp_steg

addr = 'http://web.chal.csaw.io:5018/'
r = req.get(addr).text
decoded = zwsp_steg.decode(r)
print(decoded)
```

## Hidden texts

- [`Twitter Secret Messages`](https://twsteg.devsec.fr/)

```
  i haｄ a grｅａｔ daｙ at the ｂeaｃh! #sunshｉne              
```
