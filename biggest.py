def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    keys = list(aDict.keys())
    values = list(aDict.keys())
    return keys[values.index(max(values))]