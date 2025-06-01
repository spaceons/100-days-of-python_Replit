rom getpass import getpass as input

scoreP1 = 0
scoreP2 = 0

while True:
  print("""Select your move by typing: r (rock), p (paper), s (scissors)!""")
  P1 = input("PLAYER 1 >> ")
  P2 = input("PLAYER 2 >> ")
  
  if P1 == "r":
    if P2 == "p":
      print("P2 won (PAPER) by smashing P1 (ROCK).")
      scoreP2 += 1
    elif P2 == "s":
      print("P1 (ROCK) won by smashing P2 (SCISSORS)")
      scoreP1 += 1
    elif P2 == "r":
      print("No winners here, your are both weak")
    else:
      print("Remember to typ e r,s or p.")

  elif P1 == "p":
    if P2 == "s":
      print("P2 (SCISSORS) won by smashibg P1 (PAPER)")
      scoreP2 += 1
    elif P2 == "r":
      print("P1 (PAPER) won by smashing P2 (ROCK)")
      scoreP1 += 1
    elif P2 == "p":
      print("No winners here, your are both weak")
    else:
      print("Remember to type r,s or p.")

  elif P1 == "s":
    if P2 == "r":
      print("P2 (ROCK) won by smashing P1 (SCISSORS)")
      scoreP2 += 1
    elif P2 == "p":
      print("P1 (SCISSORS) won by smashing P2 (PAPER)")
      scoreP1 += 1
    elif P2 == "s":
      print("No winners here, your are both weak")
    else:
      print("Remember to type r,s or p.")

  else:
    print("Remember to type r,s or p.")
    continue
  if scoreP1 == 3:
    print("PLAYER 1 won with", scoreP1, "point")
    break
  elif scoreP2 == 3:
    print("PLAYER 2 won with", scoreP2, "point")
    break
  else:
    continue
print("Game is over")
exit()
