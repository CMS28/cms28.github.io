import random
game = False
while game == False:
    gamerules=[["Draw","Win","Lose"],["Lose","Draw","Win"],["Win","Lose","Draw"]]
    choices = ["Rock", "Paper","Scissors"]

    #test if user is paper and computer is rock
    user = int(input("Please input 0-Rock, 1-Paper, or 2-Scissors "))
    computer = random.randint(0,2)
    print(f"You chose {choices[user]}")
    print(f"Computer chose {choices[computer]}")
    print(gamerules[computer][user])
    cont = input("Would you like to play again? ")
    if cont == "Y":
        game = False
    else:
        game = True
while game == True:
    Play = input("Would you like to start playing again? ")
    if Play == "Y":
        game = False
    else:
        game = True