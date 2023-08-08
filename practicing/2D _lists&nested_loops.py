numbers = [
    [1, 2, 3],
    [12, 44, 75, 999],
    [4, 5, 6, 7],
]

def activate():
    print(numbers[1][2])

def list():
    for x in numbers:
        for y in x:
            print(y)

list()