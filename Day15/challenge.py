# MINE:

print("""WITAJ W ANIMAL SOUNDS
""")
exit = "nie"
while exit == "nie":
  animal = input("Jakie zwierzę chcesz usłyszeć? > ") 
  if animal == "krowa":
    print("Krowa robi MUUUUU!")
  elif animal == "kot":
    print("miaAAAAAAAŁ!")
  elif animal == "pies":
    print("HAŁ HAŁ XD")
  elif animal == "wąż":
    print("SSSSSSSSSSSSSSSSSSSSSSpier... ups!")
  exit = input("Chce zakończyć grę? > ")

# replit answear:

exit = "no"
while exit == "no":
  animal_sound = input("What animal sound do you want to hear?")
  
  if animal_sound == "cow" or animal_sound == "Cow":
    print("🐮 Moo")
  elif animal_sound == "pig" or animal_sound == "Pig":
    print ("🐷 Oink")
  elif animal_sound == "sheep" or animal_sound == "Sheep":
    print ("🐑 Baaa")
  elif animal_sound == "duck" or animal_sound == "Duck":
    print("🦆 Quack")
  elif animal_sound == "dog" or animal_sound == "Dog":
    print("🐶 Woof")
  elif animal_sound == "cat" or animal_sound == "Cat":
    print("🐱 Meow")
  else: 
    print("I don't know that animal sound. Try again.")


  exit = input("Do you want to exit?: ")
