numnum = 100
num =float(input("starting number: "))

while numnum > 0:
    op = input("what do you want to do? ")
    numnum -=1
    if op == "add":
        num += float(input("the other number: "))
        print(num)
    if op == "minus":
        num -= float(input("the other number: "))
        print(num)
    if op == "multiply":
        num *= float(input("the other number: "))
        print(num)
    if op == "divide":
        num /= float(input("the other number: "))
        print(num)
    if op == "equals":
        numnum = 0
        print(num)