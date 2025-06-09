import random

myNumber = random.randint(1,1000000)
print("""Let's play a game. Guess the number that Im thinking of...""")
print()

tries = 1

while True:
  guess = int(input("What is you guess? > "))
  print()
  if guess == myNumber:
    print("""Congrats! Good answear :D""")
    break
  elif guess < myNumber:
    print("Too low, honey")
    tries += 1
    continue
  elif guess > myNumber:
    print("Too high!!")
    tries += 1
    continue

print("You tried", tries, "time/s")
