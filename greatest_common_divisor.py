def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    greatest_common_divisor = 0
    smaller = a if a > b else b

    while True:
        if (b / smaller).is_integer() and (a / smaller).is_integer():
            return smaller
        smaller -= 1
    greatest_common_divisor = smaller
    return greatest_common_divisor