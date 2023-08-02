op = input("what do you want to do?")

num1 = float(input("first number"))
num2 = float(input("second number"))
def sum():
    print(num1+num2)

def minus():
    print(num1-num2)

def divide():
    print(num1//num2)

def mult():
    print(num1*num2)

if op == "add":
    sum()
if op == "minus":
    minus()
if op == "multiply":
    mult()
if op == "divide":
    divide()