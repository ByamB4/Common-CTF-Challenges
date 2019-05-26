#!/usr/bin/python3.6
# Writen by l3yam134 on 26-05-19

values = {  '!':'1',
            '@':'2',
            '#':'3',
            '$':'4',
            '%':'5',
            '^':'6',
            '&':'7',
            '*':'8',
            '(':'9',
            ')':'0',
            ',':' '}

encodedText = "*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!"
decodedText = ''

for i in encodedText:
    decodedText += values[i]
print('Decoded text : {0}'.format(decodedText))
