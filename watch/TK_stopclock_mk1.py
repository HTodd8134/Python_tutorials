import tkinter as tk
import time
from itertools import cycle
from typing import NamedTuple


root = tk.Tk()
root.geometry("500x300")
root.title("Stopclock")

class btn(NamedTuple):
    label: str
    command: function

CYCLE = (
    btn(label="start", command=stopclock.start()),
    btn(label="stop", command=stopclock.stop())
)

class stopclock:
    def __init__(self, CYCLE):
        self.button = tk.Button(root, text=self.current_btn.label, command=switch)
        self.new_btn = cycle(CYCLE)
        self.current_btn = next(CYCLE)
        self.


    def update_time(self):
        self.time_elapsed = self.end_time - self.start_time
        counter(self.time_elapsed)

    def counter(self, secs):
        self.sec = secs
        self.mins = secs//60
        self.hours = self.mins//60
        self.display = tk.Label(root, text="{0}:{1}:{2}".format(int(self.hours), int(self.mins), int(self.sec))) 

    def switch(self):
        current_btn = next(self.new_butn)

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

instance = stopclock()
