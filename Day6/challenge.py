print("Witaj w programie!")
ready = input("Czy jesteś gotowy? > ")
if ready == "tak":
  print()
  print("Zaczynamy!")
  print()
  nazwa = input("Podaj nazwę użytkownika > ")
  haslo = input("Podaj hasło > ")
  if nazwa == "kinga" and haslo == "2505":
    print()
    print("Hej, Kochanie! <3")
  if nazwa == "paweł" and haslo == "1337":
    print()
    print("Witaj, Panie! :D")

elif ready == "nie":
  print()
  print("Wróć, gdy będziesz gotowy/a!")
  
