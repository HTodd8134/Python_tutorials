import random as rand
count = 0
winscale = 0
options = [
    "heads",
    "tails"
]
def counter(point):
    mine = input("heads or tails: ")
    comp = rand.choice(options)
    if mine == comp:
        point += 1
        print("win")
        return point
    else:
        point -=1
        print("loss")
        return point
while count != 3:
    point = counter(0)
    winscale += point
    count += 1
if (winscale >= 0):
    print("victory")
else:
    print("decimation")
