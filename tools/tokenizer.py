import nltk
#nltk.download('punkt')
#from nltk.tokenize import sent_tokenize, word_tokenize
import sys
for line in open(sys.argv[1],'r'):
    #print(sent_tokenize(line, language='english'))
    ll = nltk.tokenize.word_tokenize(line, language='english')
    print(' '.join(ll))
