import re
from collections import Counter

##def words(text): return re.findall(r'\w+', text.lower())

class Lexiconmaker:

    def __init__(self, filename='/home/lin503_myra/SWE.dict.txt'):
      
        print('start')
        self.SWE_lex = dict()
        with open (filename, mode = 'r', encoding = 'utf8') as infile:
            for line in infile:
                line = line.rstrip('\n')
                self.SWE_lex[line] = 1

        print('done')
               
    def lookup(self, word):
        if word in self.SWE_lex:
            print(self.SWE_lex[word])                    
        else:
            print('Word not in dictionary')


def main():
    swe = Lexiconmaker()
    
    
                
                
##        print('start')
##        self.SWE_lex = Counter(words(open(filename).read()))
##        print('done')       

##class Spellchecker:
##    def __init__(self, lexicon):
##        self.SWE_lexicon = lexicon
##
##
##    def find_corrections(self, files):
##        for file in files:
##            with open (file, mode = 'r', encoding = 'utf8') as textfile:
##                for line in  textfile:
##                    line = rstrip('\n')
##                 
