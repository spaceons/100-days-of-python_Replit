print("""Uzupełnij lukę w tekście.

I sprawdź, czy jesteś tak zajebisty jak ja ;)
""")
tries = 1
while True:
  print("All the ____ are closer.")
  answear = input("Odp > ")
  if answear != "stars":
    print("Spróbuj jeszcze raz")
    tries += 1
  else:
    print("Dobra robota!")
    print("Liczba prób:", tries, "!") 
    break
