import random
import time
choices = [
    "scissors", "paper", "rock"
]
playerwins = 0
compwins = 0   
num = 0
while num == 0:
    comp_choice = choices[random.randint(0, 2)]
    my_choice = input("scissors, paper, rock? ")
    print("computer picked " + comp_choice)
    time.sleep(0.5)
    if my_choice == "scissors":
        if comp_choice == "paper":
            playerwins += 1
            print("win")
        elif comp_choice == my_choice:
            print("draw")
        elif comp_choice == "rock":
            compwins += 1
            print("lose")
    elif my_choice == "paper":
        if comp_choice == "rock":
            playerwins += 1
            print("win")
        elif comp_choice == my_choice:
            print("draw")
        elif comp_choice == "scissors":
            compwins += 1
            print("lose")
    elif my_choice == "rock":
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
        num += 1
    elif  (compwins == 3):
        print("you lose!")
        num += 1
decision = input("play again?\ny or n: ")
if decision in "YyNn":
    num -=1
else:
    print("ok")


    