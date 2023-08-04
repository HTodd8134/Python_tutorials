import random
import time
choices = [
    "scissors", "paper", "rock"
]
num = 0

def pbeat():
    playerwins +=1
    print("you win")
def cbeat():
    compwins +=1
    print("you lose")
def end():
    num = 1
winlogic = {
    1: "rock",
    0: "paper",
    2: "scissors"}
while num == 0:
    playerwins = 0
    compwins = 0   
    comp_choice = choices[random.randint(0, 2)]
    my_choice = input("scissors, paper, rock? ")
    print(comp_choice)
    if my_choice == "scissors":
        if comp_choice == "paper":
            playerwins += 1
            print("win")
        elif comp_choice == my_choice:
            print("draw")
        elif comp_choice == "rock":
            compwins += 1
            print("lose")
        else:
            print("huh")
    if my_choice == "paper":
        if comp_choice == "rock":
            playerwins += 1
            print("win")
        elif comp_choice == my_choice:
            print("draw")
        elif comp_choice == "scissors":
            compwins += 1
            print("lose")
        else:
            print("huh")
    if my_choice == "rock":
        if comp_choice == "scissors":
            playerwins += 1
            print("win")
        elif comp_choice == my_choice:
            print("draw")
        elif comp_choice == "paper":
            compwins += 1
            print("lose")
        else:
            print("huh")
    if (playerwins == 3):
        print("you win!")
        break
    elif  (compwins == 3):
        print("you lose!")
        break

    