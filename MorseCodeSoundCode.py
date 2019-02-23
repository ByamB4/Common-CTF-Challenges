# Writer l3yam134 for TAMUctf 2018
# Morse code (THE CODE) decoder
# Date : 02-23-2019
# You can add keys from your problem
dicto = {
  'A':'di-dah',
  'B':'dah-di-di-dit',
  'C':'dah-di-dah-dit',
  'D':'dah-di-dit',
  'E':'dit',
  'F':'di-di-dah-dit',
  'G':'dah-dah-dit',
  'H':'di-di-di-dit',
  'I':'di-dit',
  'J':'di-dah-dah-dah',
  'K':'dah-di-dah',
  'L':'di-dah-di-dit',
  'M':'dah-dah',
  'N':'dah-dit',
  'O':'dah-dah-dah',
  'P':'di-dah-dah-dit',
  'Q':'dah-dah-di-dah',
  'R':'di-dah-dit',
  'S':'di-di-dit',
  'T':'dah',
  'U':'di-di-dah',
  'V':'di-di-di-dah',
  'W':'di-dah-dah',
  'X':'dah-di-di-dah',
  'Y':'dah-di-dah-dah',
  'Z':'dah-dah-di-dit',
  '0':'dah-dah-dah-dah-dah',
  '1':'di-dah-dah-dah-dah',
  '2':'di-di-dah-dah-dah',
  '3':'di-di-di-dah-dah',
  '4':'di-di-di-di-dah',
  '5':'di-di-di-di-dit',
  '6':'dah-di-di-di-dit',
  '7':'dah-dah-di-di-dit',
  '8':'dah-dah-dah-di-dit',
  '9':'dah-dah-dah-dah-dit'
}
def decode():
  plainText = input('Enter your text : ')
  with open (plainText, 'r') as f:
    content = f.read().strip('\n')
    content = content.split(' ')
    ans = ''
    for i in content:
      for value, key in dicto.items():
        if key == i:
          ans += value
    print('Decoded -> {0}'.format(ans))
def encode():
  plainText = input('Enter your plainText : ').upper()
  cipherText = ''
  for i in plainText:
    try:
      cipherText += dicto[i] + ' '
    except KeyError:
      cipherText += i
  print(cipherText)
if __name__ == '__main__':
  print('1) Encode')
  print('2) Decode')
  req = int(input('Your choice : '))
  if req is 2:
    decode()
  elif req is 1:
    encode()
  else:
    exit(0)
