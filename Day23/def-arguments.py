def biggerNumber(number1, number2):
  if(number1 > number2):
    print(number1, "is bigger")
  elif number1 == number2:
    print("Są równe!")
  else:
    print(number2, "is bigger")

userNumber1 = float(input("Podaj pierwszy nr > "))
userNumber2 = float(input("Podaj drugi nr > "))

userNumber1 = round(userNumber1,2)
userNumber2 = round(userNumber2,2)

biggerNumber(userNumber1,userNumber2)
