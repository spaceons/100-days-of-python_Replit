# MY GAME:

from getpass import getpass as input
print("""Select your move by typing: r (rock), p (paper), s (scissors)!""")

P1 = input("PLAYER 1 >> ")
P2 = input("PLAYER 2 >> ")

if P1 == "r":
  if P2 == "p":
    print("P2 won (PAPER) by smashing P1 (ROCK).")
  elif P2 == "s":
    print("P1 (ROCK) won by smashing P2 (SCISSORS)")
  elif P2 == "r":
    print("No winners here, your are both weak")
    
elif P1 == "p":
  if P2 == "s":
    print("P2 (SCISSORS) won by smashibg P1 (PAPER)")
  elif P2 == "r":
    print("P1 (PAPER) won by smashing P2 (ROCK)")
  elif P2 == "p":
    print("No winners here, your are both weak")

elif P1 == "s":
  if P2 == "r":
    print("P2 (ROCK) won by smashing P1 (SCISSORS)")
  elif P2 == "p":
    print("P1 (SCISSORS) won by smashing P2 (PAPER)")
  elif P2 == "s":
    print("No winners here, your are both weak")

else:
  print("Remember to type r,s or p.")

#REPLIT solution:

from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()

player1Move = input("Player 1 > ")
print()
player2Move = input("Player 2 > ")
print()

if player1Move=="R":
  if player2Move=="R":
    print("You both picked Rock, draw!")
  elif player2Move=="S":
    print("Player1 smashed Player2's Scissors into dust with their Rock!")
  elif player2Move=="P":
    print("Player1's Rock is smothered by Player2's Paper!")
  else:
    print("Invalid Move Player 2!")
elif player1Move=="P":
  if player2Move=="R":
    print("Player2's Rock is smothered by Player1's Paper!")
  elif player2Move=="S":
    print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
  elif player2Move=="P":
    print("Two bits of paper flap at each other. Dissapointing. Draw.")
  else:
    print("Invalid Move Player 2!")
elif player1Move=="S":
  if player2Move=="R":
    print("Player 2's Rock makes metal-dust out of Player1's Scissors")
  elif player2Move=="S":
    print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
  elif player2Move=="P":
    print("Player1's Scissors make confetti out of Player2's paper!")
  else:
    print("Invalid Move Player 2!")
else:
  print("Invalid Move Player 1!")
