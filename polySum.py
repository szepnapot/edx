import math

def polysum(n, s):
    '''
    Regular Polygons
    param n : number of sides
    param s : length of sides

    returns: area + square of the perimeter, rounded to 4 decimal places
    '''
    return round((0.25 * n * s**2) / math.tan(math.pi/n) + (n * s)**2, 4)