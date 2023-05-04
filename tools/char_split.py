import sys
import codecs
import string

alphas = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZY'
numbers = '0123456789'

NEW=0
ALPHA=1
NUMBER=2

inp = codecs.open(sys.argv[1] ,'r', 'utf-8').read()
sens = inp.lower().split('\n')
for i in range(len(sens)-1):
	word = ''
	mode = NEW
	#sens[i] = sens[i].replace(' ', '')
	tmpsen = []
	for j in range(len(sens[i])):
		if sens[i][j] == ' ':
			if word != '':
				tmpsen.append(word)
				word = ''
			mode = NEW
		elif sens[i][j] in alphas:
			if mode == ALPHA:
				word = word + sens[i][j]
			else:
				if word != '':
					tmpsen.append(word)
				word = sens[i][j]
			mode = ALPHA
		elif sens[i][j] in numbers:
			if mode == NUMBER:
				word = word + sens[i][j]
			else:
				if word != '':
					tmpsen.append(word)
				word = sens[i][j]
			mode = NUMBER
		else:
			#print word
			if word != '':
				tmpsen.append(word)
				word = ''
				mode = NEW
			tmpsen.append(sens[i][j])
		#print tmpsen, word
	if word != '':
		tmpsen.append(word)
	sens[i] = ' '.join(tmpsen)

output = codecs.open(sys.argv[2] ,'w', 'utf-8')
output.write('\n'.join(sens))
output.close()

