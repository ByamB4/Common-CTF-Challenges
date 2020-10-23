from requests import post

url = 'https://crypto01.chal.ctf.westerns.tokyo'
data = b'twctf: please give me the flag of\x00 2020'


res = post(url=url, data=data)

print(res.text)
