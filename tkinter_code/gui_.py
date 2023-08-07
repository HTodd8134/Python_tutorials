import tkinter as tk

def start():
    root = tk.Tk()
    label = tk.Label(root, text="message")
    label.pack(padx=10, pady=10)

    textbox = tk.Text(root, height=5)
    textbox.pack(padx=10, pady=10)

    check = tk.Checkbutton(root, text="check message box", variable= check_state)
    check.pack(padx=10, pady=10)
    check_state = tk.IntVar()

    button = tk.Button(root, text="button", command=show_message)
    button.pack(pady=10, padx=10)

    root.mainloop()

    def show_message():
        print("the button was pressed")

start()