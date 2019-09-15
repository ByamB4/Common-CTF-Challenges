#!/usr/bin/env pypy
# Writen : l3yam134
# Date   : 06-28-2019

from hashlib import sha1
import requests

# hashed = '2a55579792aa0b257fd1616ef6381a762224105d'
# salted = 'c887568b8191595708301a5600397c9d0fa08b2e973e917c433e0792c4313c64'

def find_match(hashed_string, hash_salt):
  for i in range(0, 10000):
    ans = sha1(str(i) + hash_salt).hexdigest()
    print(i, ans, hashed_string)
    if ans == hashed_string:
      print('[*] Found at {}'.format(i))
      return str(i)
  return 'gg'

def connections():
  url = 'https://ringzer0ctf.com/challenges/57'
  session = requests.Session()
  session.post('https://ringzer0ctf.com/login', data={'username':'l3yam134','password':'REDACTED'})
  response = session.get(url).text
  # print(response)
  hashed_string = str(response[response.find('----- BEGIN HASH -----<br />')+32:response.find('----- END HASH -----<br />')-10])
  salt = str(response[response.find('----- BEGIN SALT -----<br />')+32:response.find('----- END SALT -----<br />')-10])
  print((hashed_string), salt)
  # input()
  ans = find_match(hashed_string, salt)
  if ans == 'gg':
    print('ggggg')
    exit()
  url += '/' + ans
  print(url)
  print(session.get(url).text)

if __name__ == '__main__':
  connections()
