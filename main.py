import random

# Welcome Prompt, include instructions
print("Rock, Paper Scissors Against a Robot")
...
...
# Computer is going to randomly choose their weapon (Rock, Paper, Scissors)
# 1. Rock
# 2. Paper
# 3. Scissors
computerdecision = random.randint(1, 3)
# Ask their user their form of their weapon in the form of a number
print("1 = Rock")
print("2 = Paper")
print("3 = Scissors") 
print("Please choose Rock, Paper, or Scissors, Rock beats scissors, Paper beats rock, and scissors beats paper")
humandecision = int(input("Please input a number: "))
# Compare the user choice and computer choice and then tell them whether they won or loss
if(humandecision > 3):
  print("kgfnj yzrdc iog") 
elif((computerdecision == 1 and humandecision == 2) or (computerdecision == 1 and humandecision == 3) or (computerdecision == 2 and humandecision == 3)):
  print("Wow totally impressive you won against a bot")
elif((computerdecision == 2 and humandecision == 1) or (computerdecision == 3 and humandecision == 1) or (computerdecision == 3 and humandecision == 2)):
  print("Wow your so bad that you lose to a bot, get good") 
elif(computerdecision == humandecision): 
  print("Better then losing to a bot but your still bad")
print("Yes this is supposed to be dehumanzing")