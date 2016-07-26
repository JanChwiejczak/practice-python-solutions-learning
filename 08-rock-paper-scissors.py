# coding: utf-8
"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
import os

def play_game():
    choice = ''
    while choice not in ['y','yes','n','no']:
        print('Would you like to play Rock-Paper-Scissors?')
        choice = raw_input('(Y)es, (N)o: ').lower()      
    if choice in ['y', 'yes']:
        rock_paper_scissors()
    else:
        print('Bye!')
        

def rock_paper_scissors():
    possible_choices = ['r', 'p', 's']
    p1_choice = ''
    while p1_choice not in possible_choices:
        p1_choice = raw_input('Player1 please choose (R)ock, (P)aper or (S)cissors: ').lower() 
    os.system('cls')    
    p2_choice = ''
    while p2_choice not in possible_choices:
        p2_choice = raw_input('Player2 please choose (R)ock, (P)aper or (S)cissors: ') .lower()
    os.system('cls')
    outcomes = {'r': {'r': 'Draw', 'p': 'Lose', 's': 'Win'},
                'p': {'r': 'Win', 'p': 'Draw', 's': 'Lose'},
                's': {'r': 'Lose', 'p': 'Win', 's': 'Draw'}}
    p1_outcome = outcomes[p1_choice][p2_choice]
    print('Player 1 {}'.format(p1_outcome)
    
play_game()
        
