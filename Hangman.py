## Hangman Class

import string
class Hangman(object):
    '''Hangman class
            word: the numbers of tries for the word to be guessed
    '''
    
    ## Doll representing the state of the player
    doll = ['''
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

    def __init__(self,word, fix_len = 0):
        # Get secret word
        self._secret_word = word
        # Max number of trials
        self.count = len(word)+3
        # Shows the letters guessed otherwise '_'
        self.guessed_word = '_ '*len(self._secret_word)
        # The letters that have been entered by the player
        self.letters_guessed = set()                             

    # Is the word guessed
    def isTheWordGuessed(self):
        ''' Returns boolean: True if the word was discovered, False otherwise
            Test if the guess is equal to the secret_word
            It iterates over every letter in the letters guessed list
            and if they are in the secret word then sums all the numbers of its appearance'''
        if ''.join(self.letters_guessed) == self._secret_word: return True
        return False

    # Update the underlined word
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

    # Are there any trials left?
    def areThereTrials(self):
        '''Returns true if there are trials left, false otherwise '''
        return self.count <= 0

    # Doll status
    def status(self):
        '''Returns an ASCII doll representing the status of the game'''
        return self.doll[max(0, 5-self.count)]

    # Guesses left
    def guessedWord(self):
        '''Returns the guessed letter and not guessed underlined'''
        return self.guessed_word

    # Letters guessed
    def lettersGuessed(self):
        '''Returns the letters that have been guessed'''
        return ' '.join(self.letters_guessed)

    # Checks if the input is valid
    def isValidInput(self, letter):
        '''Returns true if the letter is not empty string or not an alphabet letter'''
        return True if len(letter) == 1 and letter in string.lowercase else False

    # Checks if the letter has been guessed
    def wasGuessed(self, letter):
        '''Returns True if the letter is in letters_guessed, False otherwise'''
        return True if letter in self.letters_guessed else False
        
    # Guess the whole word
    def guessWholeWord(self,word):
        '''Returns True if the word was guessed, False otherwise
            This call costs 3 trials
        '''
        self.count -= 3
        if len(word) != self._secret_word: return False
        if word == self._secret_word:
            self.letters_guessed.union(set(word))
            return True
        return True if word == self._secret_word else False

    # Guess if a letter is in the word
    def guessLetter(self,letter):
        '''Returns True if the letter is in secret word, False otherwise
            letter: the letter
        '''
        self.letters_guessed.add(letter)
        self.count -= 1
        return letter in self._secret_word

    # Get secret word at the end of a losing game
    def getSecretWord(self):
        '''Return secret word'''
        return self._secret_word

    # Get lenght of the word
    def getWordLength(self):
        '''Return an integer representing the length of the word'''
        return len(self._secret_word)

    # Get letters guessed and underscores
    def getLettersGuessed(self):
        '''Return string with the letters guessed, underscores otherwise'''
        return self.guessed_word

    # Get trials left
    def getTrialsLeft(self):
        '''Return interger representing the number if trials left'''
        return self.count








        

        
        
