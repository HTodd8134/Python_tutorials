import random as rand
count = 0
winscale = 0
def counter(point):
    mine = int(input("pick a number 1-2: "))
    num = rand.randint(0,1)
    if mine == num:
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
