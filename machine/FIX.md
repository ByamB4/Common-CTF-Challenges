### PHP

  - **Path traversal**
    ```php
    $file = basename(realpath($_GET['file']));
    include($file);
    ```
    ```php
    $file = basename($_GET['file']);
    $full_path = realpath('pages/' . $file);
    if ($full_path && is_file($full_path) && strpos($full_path, realpath('pages')) === 0) {
        include $full_path;
    } else {
        include 'pages/index.php';
    }
    ```
