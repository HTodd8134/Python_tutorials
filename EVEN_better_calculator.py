numnum = 100
num =float(input("starting number: "))

while numnum > 0:
    op = input("what do you want to do? ")
    numnum -=1
    if op == "add" or "+":
        num += float(input("next number: "))
        print(num)
    if op == "minus" or "-":
        num -= float(input("next number: "))
        print(num)
    if op == "multiply" or "*":
        num *= float(input("next number: "))
        print(num)
    if op == "divide" or "/":
        num /= float(input("next number: "))
        print(num)
    if op == "equals" or "=":
        numnum = 0
        print(num)