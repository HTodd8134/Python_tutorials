import math
import random

class game:
    def __init__(self):
        self.board = [" " for _ in range(9)]
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(" | " + " | " .join(row) + " | ")

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(" | " + " | " .join(row) + " | ")

    def possible_moves(self):
        moves =[

        ]
        return [i for i, spot in enumerate(self.board) if spot == " "]
    

    
    