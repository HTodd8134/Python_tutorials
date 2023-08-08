import tkinter as tk
import time
from itertools import cycle
from typing import NamedTuple


root = tk.Tk()
root.geometry("500x300")
root.title("Stopclock")

class btn(NamedTuple):
    label: str

CYCLE = (
    btn(label="start"),
    btn(label="stop")
)

class stopclock:
    def __init__(self, butn = CYCLE):
        self.button = tk.Button(root, text=current_btn.label, command=switch)
        self.new_btn = cycle(butn)
        current_btn = next(butn)
    
    def startup(self):
        start_time = time.time()
        update_time()

    def update_time(self):
        time_elapsed = end_time - start_time
        counter(time_elapsed)

    def counter(self, secs):
        sec = secs
        mins = secs//60
        hours = mins//60
        display = tk.Label(root, text="{0}:{1}:{2}".format(int(hours), int(mins), int(sec))) 

    def switch(self):
        current_btn = next(self.new_butn)



root.mainloop()