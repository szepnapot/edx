# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if len(lettersGuessed) < 1:
        return False
    return sum([1 for l in secretWord if l in lettersGuessed]) == len(secretWord)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed_so_far = []
    for l in lettersGuessed:
        if l in secretWord:
            guessed_so_far.append(l)
    return ''.join([l if l in guessed_so_far else '_ ' for l in secretWord])



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = list(string.ascii_lowercase[:])
    [available.remove(l) for l in lettersGuessed]
    return ''.join(available)
    
def welcome(secretWord):
    print('Welcome to the game, Hangman!\nI am thinking of a word that is {} letters long.\n-------------'.format(len(secretWord)))

def status(guesses_left, letters_guessed):
    print("You have {} guesses left.\nAvailable letters: {}".format(guesses_left, getAvailableLetters(letters_guessed)))

def getGuess():
    guess = input('Please guess a letter: ').lower()
    return guess

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_left = 8
    letters_guessed = []
    welcome(secretWord)
    while guesses_left > 0 and not (isWordGuessed(secretWord, letters_guessed)):
        status(guesses_left, letters_guessed)
        guess = getGuess()
        if guess in letters_guessed:
            print("Oops! You've already guessed that letter: {}\n-------------".format(getGuessedWord(secretWord, letters_guessed)))
        else:
            if guess not in list(secretWord):
                guesses_left -= 1
                letters_guessed.append(guess)
                print('Oops! That letter is not in my word: {}\n-------------'.format(
                    getGuessedWord(secretWord, letters_guessed)))
            else:
                letters_guessed.append(guess)
                print('Good guess: {}\n-------------'.format(getGuessedWord(secretWord, letters_guessed)))
    if isWordGuessed(secretWord, letters_guessed):
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was else.')







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
print(secretWord)
hangman(secretWord)
