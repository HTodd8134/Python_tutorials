op = int(input("1 for add, 2 for minus, 3 for multiply, 4 for divide"))

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

if op == 1:
    sum()
if op == 2:
    minus()
if op == 3:
    mult()
if op == 4:
    divide()