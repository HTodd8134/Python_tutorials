import tkinter as tk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        
        self.label = tk.Label(self.root, text="your message")
        self.label.pack(pady=10, padx=10)
        
        self.textbox = tk.Text(self.root, height=5)
        self.textbox.pack(padx=10, pady=10)

        self.check = tk.Checkbutton(self.root, text="show message box", variable = self.check_state)
        self.check.pack(padx=10, pady=10) 
        self.check_state = tk.IntVar()
        
        self.button = tk.Button(self.root, text="show message", command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()
    
    def show_message(self):
        print("button was pressed")
GUI()



def equals(num1, num2):
    if choice == 'a':
        out = num1 + num2
        return
    elif choice == 's':
        out = num1 - num2
        return
    elif choice == 'm':
        out == num1 * num2
        return
    elif choice == 'd':
        out == num1 // num2
        return
