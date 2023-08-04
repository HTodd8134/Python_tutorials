import tkinter as tk
box = tk.Tk()

box.title("GUI!")
box.geometry("800x500")
label = tk.Label(box, text = "Hello World!", font = ("Futura", 20))
label.pack(pady= 50)
text_box = tk.Text(box, height=15)

password = tk.Entry(box)

button = tk.Button(box, text="click me!", font=("Futura", 18))

frame = tk.Frame(box)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

btn1 = tk.Button(frame, text="1")
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
btn2 = tk.Button(frame, text="2")
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
btn3 = tk.Button(frame, text="3")
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
btn4 = tk.Button(frame, text="4")
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
btn5 = tk.Button(frame, text="5")
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
btn6 = tk.Button(frame, text="6")
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)
btn7 = tk.Button(frame, text="7")
btn7.grid(row=2, column=0, sticky=tk.W+tk.E)
btn8 = tk.Button(frame, text="8")
btn8.grid(row=2, column=1, sticky=tk.W+tk.E)
btn9 = tk.Button(frame, text="9")
btn9.grid(row=2, column=2, sticky=tk.W+tk.E)
btn0 = tk.Button(frame, text="0")
btn0.grid(row=3, column=1, sticky=tk.W+tk.E)





frame.pack(fill="both")


box.mainloop()