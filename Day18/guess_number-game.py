print("""Guess the number game!

CHOOSE FROM 0 to 1 000 000""")

tries = 1
number = 2400

while True:
  guess = int(input("""Guess the number 
  > """))
  if guess < 0:
    print("I will not play like that...")
    exit()
  elif guess < number:
    print("Too low")
    tries += 1
    continue
  elif guess > number:
      print("Too high")
      tries += 1
      continue
  elif guess == number:
    print("""Congrats, you win!""")
    break
  else:
    print("That in not a number, you dumb!")
    print()
    continue

print("""It takes you""", tries, "to guess")
