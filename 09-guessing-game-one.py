"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import os
from random import randint

player_guesses = {'too low': 0, 'correct': 0, 'too high': 0}

while True:
    os.system('cls')
    my_guess = randint(1,9)
    print('Guess which number I am thinking about?\nHint: I can only count to nine)')
    player_guess = int(input('Hmmm you are thinking: '))

    if player_guess == my_guess:
        print('Correct!')
        player_guesses['correct'] += 1
    elif player_guess < my_guess:
        print('You guessed too low!')
        player_guesses['too low'] += 1
    elif player_guess > my_guess:
        print('You guessed too high!')
        player_guesses['too high'] += 1
    
    if input('Shall we play another round? (Y)es or (N)o: ') in ['n', 'N', 'No', 'no']:
        break

os.system('cls')
for guess in player_guesses:
    print('You guessed {} {} times.'.format(guess, player_guesses[guess]))
    
