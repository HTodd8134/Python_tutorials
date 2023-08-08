import _tkinter as tk
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
    def __init__(self, move):
        self.board = tk.Tk()
        self.board.title("tic-tac-toe")
        self.board.mainloop()
    def setup_board(self):
        self.grid = tk.Frame(master = self.board, columnspan=3, rowspan=3)
        


class GameLogic:
    def __init__(self):
        pass