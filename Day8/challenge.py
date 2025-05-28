print("""Hej! Oto Twój generator afirmacji. 

Zadam kilka pytań, aby wywróżyć Ci coś dobrego.

              ZACZYNAJMY!
""")

name = input("Jak masz na imię? > ")
print("Hej", name, "! ""Miło Cię poznać :D")
day = input("Jaki dziś dzień tygodnia? > ")

if day == "poniedziałek" or day == "Poniedziałek" or day == "pon":
  print("""
  Oh, ciężko żyć w""", day,""". 

  No chyba, że robisz to co kochasz! Wtedy jest o wiele łatwiej.""")

elif day == "Wtorek" or day == "wtorek" or day == "wt":
  print("""
  We wtorek nosisz zgrabny worek! 
  Pieniędzy... miejmy nadzieję, bo w poniedziałek już ciężko pracowałeś.""")

elif day == "Wtorek" or day == "wtorek" or day == "wt":
  print("""
  We wtorek nosisz zgrabny worek! 
  Pieniędzy... miejmy nadzieję, bo w poniedziałek już ciężko pracowałeś.""")

elif day == "Środa" or day == "środa" or day == "śr":
  print("""
  Środa dzień... mini imprezy, bo mówi się, że to mały piątek hehe.""")

elif day == "Czwartek" or day == "czwartek" or day == "czw":
  print("""
  Czwartek dzień bez majtek! Mrrr... <3""")

elif day == "Piątek" or day == "piątek" or day == "pt":
  print("""
  Piątek weekendu początek!
            
            Nic dodać, nic ująć. Baw się dobrze... alkoholiku.""")
elif day == "sobota" or day == "niedziela":
    print("A więc weekend")
else:
  print("To nie jest dzień tygodnia...")

## Personalized - answear from replit below

print("Hello. Welcome to your daily affirmation generator.")
name = input("What is your name? ")
if name =="Mark" or name == "mark":
 DOW = input("What is the day of the week? ")
 if DOW == "monday" or DOW == "Monday":
   print("It is going to be a great Monday", name)
 if DOW == "tuesday" or DOW == "Tuesday":
   print("What a wonderful Tuesday it is", name)
 if DOW == "wednesday" or DOW == "Wednesday":
   print("Happy Hump Day", name)
 if DOW == "thursday" or DOW == "Thursday":
   print(name,"your week is almost over!")
 if DOW == "friday" or DOW == "Friday":
   print(name, "It's FRIDAY!")
   
elif name == "David" or name== "david":
 DOW = input("What is the day of the week? ")
 if DOW == "monday" or DOW == "Monday":
   print("It is going to be a great Monday", name)
 if DOW == "tuesday" or DOW == "Tuesday":
   print("You look great in that color", name)
 if DOW == "wednesday" or DOW == "Wednesday":
   print("You look chipper today", name)
 if DOW == "thursday" or DOW == "Thursday":
   print(name,"you are doing a great job!")
 if DOW == "friday" or DOW == "Friday":
   print(name, "it's FRIDAY!")
else:
 print("I do not know your name, but I hope you are having a great day!")
