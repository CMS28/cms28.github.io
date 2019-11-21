import random
# the rule of game
gamerule = [["Draw","Win","Lose"],["Lose","Draw","Win"],["Win","Lose","Draw"]]
choices = ["Rock","Paper","Scissors"]

# test if user is paper, computer is rock
#print(gamerule[0][1])

user = int(input("Please enter 0 - Rock, 1- paper, 2-Scissors: "))
computer = random.randint(0,2)

print(f"You enter {choices[user]}")
print(f"Computer choose {choices[computer]}")
print(gamerule[computer][user])