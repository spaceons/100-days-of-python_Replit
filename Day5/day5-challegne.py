print("Marvel Movie Charakter Creator")
print("--")
hanging = input("Do you like 'hanging around'?: ")
if hanging == "yes":
    print("Then you're more likely to be Spider-Man")
else: 
  print("Then you are not Spider-Man")
print()
voise = input("Do you have a 'gravelly' voice?: ")
if voise == "yes":
  print("Then you're more likely to be the Hulk")
else:
  print("Aww, so you are not the Hulk")
print()
smash = input("Do you often feel 'Marvelous'?: ")
if smash == "yes":
  print("Aha! You're Captain Marvel! Hi!")
else:
  print("Then you are not Captain Marvel")
  print()
  print("You are not Spider-Man, the Hulk or Captain Marvel")
  print("But maybe you are the next big thing in the Marvel Universe")

# Didnt know that I can use lot of 'if' with just one 'else'.
# Replit's answear below

print("Which character are you from 'Avengers?'")
print()
print("Answer these questions and let's find out.")
print()
print("Please use Y or N for yes and no.")

likeGreen = input("Do you like the color green?: ")
if likeGreen == "Y":
  print("You must be the Hulk!")

IronIsCool = input("Do you think building robots is cool?: ")  
if IronIsCool == "Y":
  print("You must be Iron Man. Cool suit!")

TimeTravel = input("Do you like traveling through time?: ")  
if TimeTravel == "Y":
  print("You must be Captain America!")

Strong = input("Are you super strong?: ")
if Strong == "Y":
  print("You have got to be Thor!")
else:
  print("I guess you are not like anyone from 'Avengers.'")  

# Przy odpowiedzi 'N' - pyta dalej.
# Przy odpowiedzi 'Y' - zgaduje i PYTA DALEJ.
