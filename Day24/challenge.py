## moja odp

import random

def rollDice():
  while True:
    roll = random.randint(1,sides)
    print("You roll", roll)
    more = input("Do you want to roll again? > ")
    if more == "yes":
      continue
    else:
      break

sides = int(input("How many sides your dice has? > "))
rollDice()

## ODP REPLIT

import random
print("Infinity Dice 🎲")
  
sides = int(input("How many sides?: "))
playGame = "yes"
  
def rollDice(sides):
  print("You rolled ", random.randint(1,sides))
while playGame == "yes":
    rollDice(sides)
    playGame = input("Roll again?")
