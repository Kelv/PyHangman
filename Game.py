## Hangman game
## Probe your lexical skill trying to beat the Hangman
## Created by Kelvin Rodriguez

## Import libraries
import random
import string
import os
from Hangman import *
from WordGenerator import *


class Game():
    '''Class for playing the game'''

    def tryAgain(self):
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

    def Play(self,hangman):
        '''hangman: hangman object to play with
           return: boolean indication if want to play again
           Method where the game process takes place

            * When the game starts it lets you know the length of the word

            * Ask the player to guess a letter

            * The user will receive feedback of his choice

            * And will display the word with the characters guessed so far
        '''
                    
        print "Welcome to the Hangman Game"
        print "I have a word that I want you to guess and it is "+str(hangman.getWordLength())+" letters long"
        print "-------------------------------------------------------------------------"

        while True:
            # If the word has benn guessed
            if hangman.isTheWordGuessed():
                '''If the word is guessed the end the game and ask if want to try again'''
                print "Congratulations!!! You have won!!! The word was " + hangman.getSecretWord()
                return self.tryAgain()
            # If there are no more trials left
            if hangman.getTrialsLeft() <= 0:
                '''If the word is not guessed and there are no more guesses left
                    then end the game and ask if want to try again'''
                print hangman.status()
                print "Sorry, you have lost. The word was " + hangman.getSecretWord()
                return self.tryAgain()

            ##os.system('clear')
            # Status
            print "-------------------------------------------------------------------------"
            # Print the doll
            print hangman.status()
            print "You have "+ str(hangman.getTrialsLeft())+" guesses left"
            print hangman.guessedWord()
            if len(hangman.lettersGuessed()) > 0:
                print ("The letters you have entered are: " + hangman.lettersGuessed())

            # Get letter
            letter = raw_input("Enter your guess ").lower()
            # If is the whole word being guessed
            if len(letter) == hangman.getWordLength():
                if hangman.guessWholeWord(letter):
                    print "You Guessed Correct!!"
                else:
                    print "Sorry, that was not the word"
            # If its not a valid input
            elif not hangman.isValidInput(letter):
                print "Thats not a valid input. Please try again"
            # If has been guessed
            elif hangman.wasGuessed(letter):
                print "You already guessed that one"
            # If its a valid input then its ok to guess
            else:
                if hangman.guessLetter(letter):
                    print "You Guessed Correct!!"
                    hangman.newGuessedWord()
                else:
                    print "OOhh!! Sorry, that one wasn't in the word"

    ## Start the game
    def Start(self, diff = 0):
        '''diff: difficulty, lenght of the word from 2 to 10 otherwise random
            Start playing the game '''
        # Instance of wordGenerator
        wordGenerator = WordGenerator()
        # Play control
        play = True
        while play:
            # Create instance of hangman
            h = Hangman(wordGenerator.generate(diff))
            # Start game and wait for response
            play = self.Play(h)
        print "Thank you for playing"
    
# Start game                    
Game().Start()
