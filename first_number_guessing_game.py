import random as rand
wins = 0
losses = 0
def win():
    print("win")
    wins += 1
def lose():
    print("lose")
    losses += 1

while (wins != 3) and (losses != 3):
     mine = int(input("pick a number 1-2: "))
     num = rand.randint(0,1)
     if mine == num:
        wins += 1
        print("you have " + str(wins) + " wins")
     else:
        losses += 1
        print("you have " + str(losses) + " losses")
if (wins == 3):
    print("victory")
else:
    print("decimation")