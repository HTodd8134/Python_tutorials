numnum = 100
num =float(input("starting number: "))

while numnum > 0:
    op = input("what do you want to do? ")
    numnum -=1
    if op == "+":
        num += float(input("next number: "))
        print(num)
    elif op == "-":
        num -= float(input("next number: "))
        print(num)
    elif op == "*":
        num *= float(input("next number: "))
        print(num)
    elif op == "/":
        num /= float(input("next number: "))
        print(num)
    elif op == "=":
        numnum = 0
        print(num)