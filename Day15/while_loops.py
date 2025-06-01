# infinite loop:
counter = 0
while counter < 10:
  print(counter)

# fixed:
counter = 0
while counter < 10:
  print(counter)
  counter += 1

# dlaczego ""?
exit = ""
while exit = "yes":
  print("🥳")
exit = input("Exit?: ")
