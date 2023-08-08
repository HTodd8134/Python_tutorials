import tkinter as tk

calculation = ""

def add_to_calc(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)

    except:
        clear()
        text_result.insert(1.0, "Error")

def clear():
     global calculation
     calculation = ""
     text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("324x154")
root.title("Calculator")

text_result = tk.Text(root, height=2, width=25, font=24)
text_result.grid(columnspan=5)

btn1 = tk.Button(root, text="1", width=5, command=lambda: add_to_calc(1))
btn1.grid(row=2, column=0)
btn2 = tk.Button(root, text="2", width=5, command=lambda: add_to_calc(2))
btn2.grid(row=2, column=1)
btn3 = tk.Button(root, text="3", width=5, command=lambda: add_to_calc(3))
btn3.grid(row=2, column=2)
btn4 = tk.Button(root, text="4", width=5, command=lambda: add_to_calc(4))
btn4.grid(row=3, column=0)
btn5 = tk.Button(root, text="5", width=5, command=lambda: add_to_calc(5))
btn5.grid(row=3, column=1)
btn6 = tk.Button(root, text="6", width=5, command=lambda: add_to_calc(6))
btn6.grid(row=3, column=2)
btn7 = tk.Button(root, text="7", width=5, command=lambda: add_to_calc(7))
btn7.grid(row=4, column=0)
btn8 = tk.Button(root, text="8", width=5, command=lambda: add_to_calc(8))
btn8.grid(row=4, column=1)
btn9 = tk.Button(root, text="9", width=5, command=lambda: add_to_calc(9))
btn9.grid(row=4, column=2)
btn0 = tk.Button(root, text="0", width=5, command=lambda: add_to_calc(0))
btn0.grid(row=5, column=1)
btne = tk.Button(root, text="=", width=5, command=lambda: evaluate())
btne.grid(row=5, column=2)
btnc = tk.Button(root, text="c", width=5, command=lambda: clear())
btnc.grid(row=5, column=0)
btna = tk.Button(root, text="+", width=5, command=lambda: add_to_calc("+"))
btna.grid(row=2, column=4)
btnm = tk.Button(root, text="-", width=5, command=lambda: add_to_calc("-"))
btnm.grid(row=3, column=4)
btnt = tk.Button(root, text="*", width=5, command=lambda: add_to_calc("*"))
btnt.grid(row=4, column=4)
btnd = tk.Button(root, text="/", width=5, command=lambda: add_to_calc("/"))
btnd.grid(row=5, column=4)

root.mainloop()