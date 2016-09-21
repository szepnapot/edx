def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    return tuple((e for i, e in enumerate(aTup) if i % 2 == 0))