def login():
  while True:
    Name = input("What's your nickname? > ")
    Password = input("What's your pasword? > ")
    if Name == "pawlak" and Password == "spaceons":
      break
    else:
      print("Wrong password or nickname")
      continue

login()
print("Welcome to your base!")
