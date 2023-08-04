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
    print("well i picked " + comp_choice)
    time.sleep(0.5)
    for choice in choices:
        
    
    if (playerwins == 3):
        print("you win!")
        num += 1
    elif  (compwins == 3):
        print("you lose!")
        num += 1

    