# coding: utf-8
"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

def play_game():
    choice = ''
    while choice not in ['y','yes','n','no']:
        print('Would you like to play Rock-Paper-Scissors?')
        choice = raw_input('(Y)es, (N)o: ').lower()      
    if choice in ['y', 'yes']:
        print('pass - playing game')
    else:
        print('Bye!')
        
play_game()