import tkinter as tk
root = tk.Tk()
root.geometry("250x210")
label = tk.Label(root, text = "Calculator")
label.pack(pady=3)
text_box = tk.Text(root, height=4)
text_box.pack()

numone = "0"
numtwo = "0"
numthree = "0"


frame = tk.Frame(root)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)
    
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


btequals = tk.Button(frame, text="=")
btequals.grid(row=3, column=2, sticky=tk.W+tk.E)


btback = tk.Button(frame, text="<-")
btback.grid(row=3, column=0, sticky=tk.W+tk.E)


btadd = tk.Button(frame, text="+")
btadd.grid(row=0, column=3, sticky=tk.W+tk.E)


btmin = tk.Button(frame, text="-")
btmin.grid(row=1, column=3, sticky=tk.W+tk.E)


btdiv = tk.Button(frame, text="/")
btdiv.grid(row=2, column=3, sticky=tk.W+tk.E)


btmult = tk.Button(frame, text="*")
btmult.grid(row=3, column=3, sticky=tk.W+tk.E)


frame.pack(fill="both")


root.mainloop()