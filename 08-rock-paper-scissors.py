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
        choice = input('(Y)es, (N)o: ').lower()      
    if choice in ['y', 'yes']:
        rps = RockPaperScissorsGame()
        rps.play()
    else:
        print('Bye!')
        
class RockPaperScissorsGame:
    possible_choices = ['r', 'p', 's']
    outcomes = {'r': {'r': 'Draw', 'p': 'Lose', 's': 'Win'},
                'p': {'r': 'Win', 'p': 'Draw', 's': 'Lose'},
                's': {'r': 'Lose', 'p': 'Win', 's': 'Draw'}}

    def ask_for_player_choice(self, choice=None):
        os.system('cls')
        while choice not in self.possible_choices:
            choice = input('Please choose (R)ock, (P)aper or (S)cissors: ').lower()
        return choice    

    def play(self):
        self.p1_choice = self.ask_for_player_choice()
        self.p2_choice = self.ask_for_player_choice()
        self.p1_outcome = self.outcomes[self.p1_choice][self.p2_choice]
        print('{} for Player 1'.format(self.p1_outcome))

play_game()
