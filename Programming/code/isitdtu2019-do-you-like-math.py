from pwn import *
s = remote("104.154.120.223", 8083)
while(1):
	text = s.recv()
	print text
	lines = text.split('\n')[1:-1]
	num_dict = {
	'0' : '  ###  \n #   # \n#     #\n#     #\n#     #\n #   # \n  ###  \n       ',
	'1' : '  #  \n ##  \n# #  \n  #  \n  #  \n  #  \n#####\n     ',
	'2' : ' ##### \n#     #\n      #\n ##### \n#      \n#      \n#######\n       ',
	'3' : ' ##### \n#     #\n      #\n ##### \n      #\n#     #\n ##### \n       ',
	'4' : '#      \n#    # \n#    # \n#    # \n#######\n     # \n     # \n       ',
	'5' : '#######\n#      \n#      \n###### \n      #\n#     #\n ##### \n       ',
	'6' : ' ##### \n#     #\n#      \n###### \n#     #\n#     #\n ##### \n       ',
	'7' : '#######\n#    # \n    #  \n   #   \n  #    \n  #    \n  #    \n       ',
	'8' : ' ##### \n#     #\n#     #\n ##### \n#     #\n#     #\n ##### \n       ',
	'9' : ' ##### \n#     #\n#     #\n ######\n      #\n#     #\n ##### \n       ',
	'*':'       \n #   # \n  # #  \n#######\n  # #  \n #   # \n       \n       ',
	'-':'     \n     \n     \n#####\n     \n     \n     \n     ',
	'+':'     \n  #  \n  #  \n#####\n  #  \n  #  \n     \n     '
	}
	equation = ''
	for j in range(5):
		index = 0
		text = ''
		while(1):
			for l in lines:
				text += l[index]
			if text != '        ':
				index += 1
				text = ''
			else:
				break
		num = '\n'.join([l[:index] for l in lines])
		for key,value in num_dict.iteritems():
			if value == num:
				equation += key
		for i in range(len(lines)):
			lines[i] = lines[i][index+1:]
	s.sendlineafter('>>> ',str(eval(equation)))
	print str(eval(equation))
