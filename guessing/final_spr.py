import random as rand

def play():
    player = input("'p' for paper, 'r' for rock, 's' for scissors:\n")
    comp = rand.choice(["p", "s", "r"])
    if player == comp:
        return "tie"
    if wins(player, comp):
        return "you win!"
    else:
        return "you lose!"

def wins(user, computer):
    if (user == "p" and computer == "r") or (user == "r" and computer == "s") or (user == "s" and computer == "p"):
        return True
    
print(play())
    
