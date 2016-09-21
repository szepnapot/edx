secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']


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

print(getGuessedWord(secretWord, lettersGuessed))