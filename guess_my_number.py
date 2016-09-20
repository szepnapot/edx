min = 0
max = 100

print('Please think of a number between 0 and 100!')
while True:
    guess = int((min + max) / 2)
    while True:
        print("Is your secret number {}?".format(guess))
        user_inp = input("Enter 'h' to indicate the guess is too high. "
                         "Enter 'l' to indicate the guess is too low. "
                         "Enter 'c' to indicate I guessed correctly.")
        if user_inp in 'hlc':
            break
        else:
            print('Sorry, I did not understand your input.')
    if user_inp == 'l':
        min = guess
    elif user_inp == 'h':
        max = guess
    elif user_inp == 'c':
        print('Game over. Your secret number was: {}'.format(guess))
        break


