from Tic_Tac_Toe_Player import HumanPlayer, RandomComputerPlayer
import time

class Tic_Tac_Toe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #assigns index to each space in a 3x3 grid
        self.current_winner = None  #to keep track of if there is a winner

    def print_board(self):
        #just getting the rows
        for row in [self.board[i*3:(i+1)*3]for i in range(3)]: #row 1 would be index 0-2, row 2 would be 3-5, row 3 would be 6-8
            print('| ' + ' | '.join(row) + ' |') # | is a separator
    
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def avaliable_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' '] 
        #create tuple [index, spot] and puts index number from print board nums function in the spot if the spot is empty
    def empty_squares(self):
        return ' ' in self.board  
        #returns any empty squares in the board
    def num_empty_squares(self):
        return self.board.count(' ')
        #counts how many spaces in the board
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner=letter
            return True
        return False  
    def winner(self, square, letter):
        #winning conditions
        #checking row first
        #need to divide index by 3
        row_index = square//3
        row=self.board[row_index*3: (row_index +1) *3 ]
        if all ([spot == letter for spot in row]) :
            return True
        #checking column 
        # need to modulus index by 3
        #for every single row (i) if we add the column index. we will get every singe value in that column 
        col_index = square % 3
        col=[self.board[col_index+i*3] for i in range(3)] 
        if all ([spot == letter for spot in col]) :
            return True
        #checking diagonal  
        # needs to be even number (0,2,4,6,8)
        if square % 2 ==0:
            diag1= [self.board[i] for i in [0,4,8]] #left to right diagonal
            if all ([spot == letter for spot in diag1]) :
                    return True
            diag2= [self.board[i] for i in [2,4,6]] #right to left diagonal
            if all ([spot == letter for spot in diag2]) :
                    return True    
        return False



def play(game,x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    letter = 'X'  
    
    #actual game logic below
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else: 
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')  
                game.print_board()  
                print('')
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!') 
                return letter    


            letter = "O" if letter == 'X' else 'X'  
            time.sleep(0.8)
    if print_game:
        print('It\'s a tie')   
if __name__== '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t=Tic_Tac_Toe()
    play(t, x_player, o_player, print_game= True)



        


    