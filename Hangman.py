## Hangman game
## Probe your lexical skill trying to beat the Hangman
## Created by Kelvin Rodriguez

import random
import string
import os


mun = ['''
         **
        *  *
         **
         ||
        /||\\   
       / || \\
        /  \\
       /    \\

''','''
         **
        *  *
         **
         ||
         ||\\   
         || \\
        /  \\
       /    \\

''','''
         **
        *  *
         **
         ||
         ||   
         ||
        /  \\
       /    \\

''','''
         **
        *  *
         **
         ||
         ||   
         ||
           \\
            \\

''','''
         **
        *  *
         **
         ||
         ||   
         ||
        
       

''','''
           |
        ** |
       *  *|
        **|| 
          ||   
          ||
        
       

''']

class SecretWordGenerator:
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


class Hangman(object):
    '''Hangman class
            trials(optional): the numbers of tries for the word to be guessed
            fix_len(optional): the length of the word to be guessed'''
    
    def __init__(self,trials = 8, fix_len = 0):
        # Create an instance of SecretWordGenerator
        self.secret_word_gen = SecretWordGenerator()
        # Generate a secret word
        self._secret_word = self.secret_word_gen.generate(length = fix_len if fix_len > 1 else 0)   
        # Max number of trials
        self.count = trials
        # Shows the letters guessed otherwise '_'
        self.guessed_word = '_ '*len(self._secret_word)
        # The letters that have been entered by the player
        self.letters_guessed = []                             

    ## Helper Methods:        
    def isTheWordGuessed(self):
        ''' Returns boolean: True if the word was discovered, False otherwise
            Test if the guess is equal to the secret_word
            It iterates over every letter in the letters guessed list
            and if they are in the secret word then sums all the numbers of its appearance'''
        c = 0
        sw = self._secret_word
        for i in self.letters_guessed:  
            if i in sw:
                c += sw.count(i)
                
        if c == len(self._secret_word): return True
        return False

    
    def newGuessedWord(self):
        '''Change the guessed_word to its new values replacements'''
        new_guessed_word = []
        sw = self._secret_word
        for i in range(len(sw)):
            if sw[i] in self.letters_guessed:
                new_guessed_word.append(sw[i]+' ')
            else:
                new_guessed_word.append('_ ')
        self.guessed_word = ''.join(new_guessed_word)                    

    def Play(self):
        ''' Method where the game process takes place

            * When the game starts it lets you know the length of the word

            * Ask the player to guess a letter

            * The user will receive feedback of his choice

            * And will display the word with the characters guessed so far

            * Returns boolean: True to play again, False otherwise
        '''
        
        def tryAgain():
            '''Request if the player wants to play again or not
            returns: boolean, True if the player want to play again
                     False if he doesnt'''
            while True:
                    op = raw_input("Do you want to try again? [y/n]").lower()
                    if op == 'y':
                        return True
                    elif op == 'n':
                        return False
                    else:
                        print "I didn't get that"
                    
        print "Welcome to the Hangman Game"
        print "I have a word that I want you to guess and it is "+str(len(self._secret_word))+" letters long"
        print "-------------------------------------------------------------------------"

        while True:
        
            if self.isTheWordGuessed():
                '''If the word is guessed the end the game and ask if want to try again'''
                print "Congratulations!!! You have won!!! The word was "+self._secret_word
                return tryAgain()

            if self.count <= 0:
                '''If the word is not guessed and there are no more guesses left
                    then end the game and ask if want to try again'''
                print mun[5]
                print "Sorry, you have lost. The word was "+self._secret_word
                return tryAgain()

            os.system('cls')
            print "-------------------------------------------------------------------------"
            print mun[max(0,5-self.count)]
            print "You have "+ str(self.count)+" guesses left"
            print self.guessed_word
            if len(self.letters_guessed) > 0:
                print ("The letters you have entered are: "+' '.join(self.letters_guessed))
            
            letter = raw_input("Enter your guess ").lower()
            if len(letter) != 1 or not letter in string.lowercase:
                print "Thats not a valid input. Please try again"
                continue
            if letter in self.letters_guessed:
                print "You already guessed that one"
                continue
            else:
                self.letters_guessed.append(letter)
                self.count -= 1
                self.newGuessedWord()
                if letter in self._secret_word:
                    print "You Guessed Correct!!"
                else:
                    print "OOhh!! Sorry, that one wasn't in the word"
                

class Game():
    '''Class for playing the game'''
    ## Start the game
    def Play(self, diff = 0):
        '''diff: difficulty, lenght of the word from 2 to 10 otherwise random
            Start playing the game '''
        play = True
        while play:
            h = Hangman(fix_len = diff)
            play = h.Play()
        print "Thank you for playing"
                        
Game().Play()






        

        
        
