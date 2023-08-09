import tkinter as tk
from typing import NamedTuple
from itertools import cycle

class default_players(NamedTuple):
    tag: str

players = (
    default_players(tag="x"),
    default_players(tag="O")
)


class Player:
    def __init__(self, player_list = players):
        self.current_player = cycle(player_list)
        self.starting_player = next(self.current_player)


class Board:
    def __init__(self):
        self.board = tk.Tk()
        self.board.title("tic-tac-toe")
        self.setup_board()
        self.board.mainloop()
    
    def setup_board(self):
        self.grids = tk.Frame(master = self.board)
        for row in range(3):
            self.columnconfigure(row, weight=1)
            self.rowconfigure(row, weight=1)
            for col in range(3):
                btn = tk.Button(self.board,)


class GameLogic:
    def __init__(self):
        pass
def main():
    baord = Board()

if __name__ == "__main__":
    main()