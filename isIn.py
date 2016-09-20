def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    if len(aStr) == 1:
        return True if aStr == char else False
    else:
        if aStr[(len(aStr)) // 2] > char:
            return isIn(char, aStr[:(len(aStr)) // 2])
        else:
            return isIn(char, aStr[(len(aStr)) // 2:])