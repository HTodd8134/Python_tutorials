import tkinter as tk
from itertools import cycle
from typing import NamedTuple

class Player(NamedTuple):
    label: str
    colour: str

class Move(NamedTuple):
    row: int
    col: int
    label: str = ""

PLAYERZ = [
    Player(label="X", colour="Green"),
    Player(label="O", colour="Blue")
]

class GAME:
    def __init__(self, players = PLAYERZ):
        self.user = cycle(players)
        self.current_player = next(self.user)
        self.current_moves = []
        self.winning_combos = []
        self.winning_move = []
        self.is_winner = False
        self.setup_board()
    
    def setup_board(self):
        self.current_moves = [
            [Move(row, col) for col in range(3)
             for row in range(3)]
        ]
        self.winning_combos = self.find_winning_combos()

    def find_winning_combos(self):
        rows = [[(move.row, move.col) for move in row] for row in self.current_moves]
        cols = [[(move.row,move.col)for move in col]for col in self.current_moves]
        first_diagonal = [row[i] for i,row in enumerate(rows)]
        second_diagonal = [col[i] for i,col in enumerate(reversed(cols))]
        return rows + cols + [first_diagonal, second_diagonal]
    
    def switch_player(self):
        self.current_player = next(self.user)

    def is_valid_move(self, move):
        row = move.row
        col = move.col
        no_winner = not self.is_winner
        move_not_played = self.current_moves[row][col].label == ""
        return no_winner and move_not_played
    
    def process_move(self, move):
        row = move.row
        col = move.col
        self.current_moves[row][col] = move
        for combo in self.winning_combos:
            results = set(self.current_moves[x][y].label for x, y in combo)
            is_win = len(results == 1) and ("" not in results)
            if is_win:
                self.is_winner = True
                self.winning_move = combo
                break

    def has_winner(self):
        return self.is_winner
    
    def is_tied(self):
        no_winner = not self.is_winner
        player_moves = (
            move.label for row in self.current_moves for move in row
        )
        return no_winner and all(player_moves)
    
class BOARD(tk.Tk):
    def __init__(self, Game):
        super().__init__()
        self.title("Tic-Tac-Toe")
        self.game = Game
        self.cells = {}

    def create_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill="x")
        self.display = tk.Label(
            master = display_frame,
            text = "click a square to begin",
        )
        self.display.pack()

    def create_board(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(3):
            self.rowconfigure(row, weight=1)
            self.columnconfigure(row, weight=1)
            for col in range(3):
                btn = tk.Button(master=grid_frame, text="", fg="Black", width=3, height=2, highlightbackground="Lightblue")
                self.cells = [btn] = (row, col)
                btn.bind("<ButtonPress-1>", self.play) 
                btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    
    def play(self, event):
        clicked_btn = event.widget
        row, col = self.cells(clicked_btn)
        move = Move(row, col, self.game.current_player.label)
        if self.game.is_valid_move(move):
            self.update_button(clicked_btn)
            if self.game.is_tied():
                self.update_display(new_text="tie", colour="red")
            elif self.game.is_winner:
                self.highlight_squares()
                new_text = f"player '{self.game.current_player.label}' won"
                colour = self.game.current_player.colour
                self.update_display(new_text, colour)
            else:
                self.game.switch_player()
                new_text = f"player '{self.game.current_player.label}'s turn"
                self.update_display(new_text)

    def update_button(self, clicked_btn):
        clicked_btn.config(text=self.game.current_player.label, fg=self.game.current_player.colour)

    def update_display(self, new_text, colour):
        self.display["text"] = new_text
        self.display["color"] = colour

    def highlight_squares(self):
        for btn, coordinates in self.cells.items():
            if coordinates in self.winning_move:
                btn.config(highlightbackground="red")

def main():
    gam = GAME()
    boar = BOARD(gam)
    boar.mainloop()

if __name__ == "__main__":
    main()
