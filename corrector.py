from lexiconmaker import Lexiconmaker

class Corrector:

    def __init__(self, dictfile='/home/lin503_myra/SWE.dict.txt', learnerfile='/home/lin503_myra/01_ASU.txt'):
        
        self.wordlist = []
        self.SWE_lex = dict()
        
        with open (dictfile, mode = 'r', encoding = 'utf8') as infile:
            for line in infile:
                line = line.rstrip('\n')
                self.SWE_lex[line] = 1

    
        with open (learnerfile, mode = 'r', encoding = 'utf8') as datafile:
            for line in datafile:
                line = line.rstrip('\n')
                if line == '.':
                    continue
                else:
                    self.wordlist.append(line)


    def edits2(self, word): 
        "All edits that are two edits away from `word`."
        return (e2 for e1 in edits1(word) for e2 in edits1(e1))

    def edits1(self, word):
        "All edits that are one edit away from `word`."
        letters    = 'abcdefghijklmnopqrstuvwxyz'
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
        inserts    = [L + c + R               for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)


    def known(self, words): 
        "The subset of `words` that appear in the dictionary of SWE_lex."
        return set(w for w in words if w in self.SWE_lex)


    def candidates(self, word): 
        "Generate possible spelling corrections for word."
        return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

    def listcorrection(self):
        ## generates a list of words
        corrected_words = []
        for word in self.wordlist:
            corrected_words.append(candidates(word))
        return corrected_words

                                







def main():
    swe = Corrector()
    swe.listcorrection()
