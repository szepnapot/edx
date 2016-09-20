epsilon = 0.01
y = float(input('Enter number to find its square root: '))
guess = y / 2.0
numGuesses = 0

while abs(guess * guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - ((guess**2 - y) / (2 * guess))
print('numGuesses = {}'.format(numGuesses))
print('Square root of {} is about {}'.format(y, guess))
