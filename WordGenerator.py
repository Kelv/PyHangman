## Word Generator
import string
import random

class WordGenerator():
    ''' Class for generating random words '''


    def __init__(self):
        '''Initialization of words generator
            Loads a file of english words and parses it to a list of words
        '''
        f = open('words.txt', 'r', 0)
        self._word_list = string.split(f.readline())
        
        
    def generate(self, length = 0):
        ''' Generates a random word from the list of words'''
        if length <= 1 or length > 10:
            return random.choice(self._word_list)
        while True:
            word = random.choice(self._word_list)
            if len(word) == length:
                return word
