# Rock Paper Scissors
import random
choiceList = ["Rock", "Paper", "Scissors"]

def getWinner(PC, Player):
    if PC == "Rock" and Player == "Rock":
        return 0
    
    if PC == "Rock" and Player == "Paper":
        return "Player"
    
    if PC == "Rock" and Player == "Scissors":
        return "PC"
    # -------------------------------------------------- #
    if PC == "Paper" and Player == "Rock":
        return "PC"
    
    if PC == "Paper" and Player == "Paper":
        return 0
    
    if PC == "Paper" and Player == "Scissors":
        return "Player"
    # -------------------------------------------------- #
    if PC == "Scissors" and Player == "Rock":
        return "Player"
    
    if PC == "Scissors" and Player == "Paper":
        return "PC"
    
    if PC == "Scissors" and Player == "Scissors":
        return 0

while True:
    playerInput = input("Rock, Paper or Scissors? ")
    pcChoice = random.choice(choiceList) #DO NOT NAME ANOTHER FOLDER RANDOM.PY

    getWinnerValue = getWinner(pcChoice, playerInput)
    if getWinnerValue == "Player":
        print(f"PC chose {pcChoice}, Player wins")
        break
    elif getWinnerValue == "PC":
        print(f"PC chose {pcChoice}, PC wins")
    elif getWinnerValue == 0:
        print(f"PC chose {pcChoice}, DRAW")