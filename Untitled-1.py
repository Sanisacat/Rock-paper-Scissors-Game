from random import randint
import time

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,1)]

player = False

while player == False: #set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("computer choses ", computer)
            time.sleep(1)
            print("You lose!", computer, "covers", player)
        else :
            print("computer choses ", computer)
            time.sleep(1)
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("computer choses ", computer)
            time.sleep(1)
            print("You lose!", computer, "cut", player)
        else :
            print("computer choses ", computer)
            time.sleep(1)
            print("You win!", player, "covers", computer)
    
    elif player == "Scissors":
        if computer == "Rock":
            print("computer choses ", computer)
            time.sleep(1)
            print("You lose...", computer, "smashes", player)
        else :
            print("computer choses ", computer)
            time.sleep(1)
            print("You win!", player, "cut", computer)
    else :
        print("That's not a valid play. Check your spelling!")# player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0, 1)]