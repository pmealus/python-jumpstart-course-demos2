import random

print('-' * 15)
print(' ' * 5 + 'GUESS THE NUMBER APP')
print('-' * 15)

the_number = random.randint(0,100)
guess = -1


while guess != the_number:

    guess_txt = input('Guess a number between 0 - 100: ')
    guess = (int(guess_txt))

    if int(guess) > the_number:
        print('Too High, try again')
    elif int(guess) < the_number:
        print('Too Low, try again')
    else:
        print('You got it!')


print('Done!')



