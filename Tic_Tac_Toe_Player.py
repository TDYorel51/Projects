import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter
        #letter is X or O

    #all players to get their next move given a game    
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        square = random.choice(game.avaliable_moves())
        return square   
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        valid_square = False
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):') 
            try:
                #trys to see if the square is avaliable. if it is not avaliable, then it throws an error
                value =int(square)
                if value not in game.avaliable_moves():
                    raise ValueError
                valid_square=True  
            except ValueError:
                print('Invalid square, Try again.')    
        return value          
    
