from datetime import date
# import marisa_trie
from random import choice

from text_helpers import is_ascii


class PolishDict():
    def __init__(self):
        self.words = ["NONE"]
        pass
        # self.load_Tries()
        #trie and reverse trie

    def random_word(self):
        return choice(self.words)

    def load_Tries(self):
        self.load_Trie()
        self.load_reverse_Trie()
        pass

    def load_Trie(self):
        print("Loading Dictionary")
        self.words = []
        with open("dictionaries/alfabet.txt","r") as alfabet:
            for word in alfabet:
                word = word[:-1]
                if is_ascii(word):
                    self.words.append(word)
            # self.words = alfabet.readlines()
        print("Dictionary loaded")

    def load_reverse_Trie(self):
        pass


if __name__ == "__main__":
    polishDict = PolishDict()
    print(repr(polishDict.random_word()))
    print(repr(polishDict.random_word()))
    print(repr(polishDict.random_word()))
    print(repr(polishDict.random_word()))
