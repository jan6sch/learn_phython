
unvalid_player = True
while unvalid_player == True:
  
  player = int(input("How much people play? (1/2) "))

  if 2 >= player > 0 :
    unvalid_player = False
  elif player > 2:
    print("\nMax two people at the same time")
    unvalid_player = True
  else :
    print("\nMin 1 person has to play")
    unvalid_player = True

winsp1 = 0
winsp2 = 0
draws = 0
rounds = 1
minirounds = 0
nowin = True
nodraw = True
unvaldicall = True
field1 = "1"
field2 = "2"
field3 = "3"
field4 = "4"
field5 = "5"
field6 = "6"
field7 = "7"
field8 = "8"
field9 = "9"

def print_board(): print(f"\n\n{field1} | {field2} | {field3}\n{field4} | {field5} | {field6}\n{field7} | {field8} | {field9}\n")

def check_valid_p1(call):

  global field1, field2, field3, field4, field5, field6, field7, field8, field9, unvaldicall

  if call in [field1, field2, field3, field4, field5, field6, field7, field8, field9]:
    print("Valid call")
    if call == field1:
      field1 = symbolp1
    elif call == field2:
      field2 = symbolp1
    elif call == field3:
      field3 = symbolp1
    elif call == field4:
      field4 = symbolp1
    elif call == field5:
      field5 = symbolp1
    elif call == field6:
      field6 = symbolp1
    elif call == field7:
      field7 = symbolp1
    elif call == field8:
      field8 = symbolp1
    elif call == field9:
      field9 = symbolp1
    unvaldicall = False
  else:
    print("Unvalid call")



def check_valid_p2(call):

  global field1, field2, field3, field4, field5, field6, field7, field8, field9, unvaldicall

  if call in [field1, field2, field3, field4, field5, field6, field7, field8, field9]:
    print("Valid call")
    if call == field1:
      field1 = symbolp2
    elif call == field2:
      field2 = symbolp2
    elif call == field3:
      field3 = symbolp2
    elif call == field4:
      field4 = symbolp2
    elif call == field5:
      field5 = symbolp2
    elif call == field6:
      field6 = symbolp2
    elif call == field7:
      field7 = symbolp2
    elif call == field8:
      field8 = symbolp2
    elif call == field9:
      field9 = symbolp2
    unvaldicall = False
  else:
    print("Unvalid call")

def check_winner():
  global combinations
  combinations = [
          [field1, field2, field3],  # oben
          [field4, field5, field6],  # mitte
          [field7, field8, field9],  # unten
          [field1, field4, field7],  # links
          [field2, field5, field8],  # mitte
          [field3, field6, field9],  # rechts
          [field1, field5, field9],  # diagonal \
          [field3, field5, field7],  # diagonal /
  ]


  for combo in combinations:
    print("Prüfe:", combo)  # debug: zeigt aktuelle Reihe
    if combo[0] == combo[1] == combo[2]:
      return combo[0]
  return None
  


unvalid_symbol = True
if player == 1 :
  while unvalid_symbol == True:
    symbol = str(input("\nWhich symbol do you wanna play? (X/O) "))
    symbol = symbol.upper()
    if symbol == "X" or symbol == "O":
      print(f"\nYou play as {symbol}")
      unvalid_symbol = False
    else :
      print("Unvalid input")
  print("while geschafft")








else:
  while unvalid_symbol == True:
    symbolp1 = str(input("\nWhich symbol does Player1 play (X/O) "))
    symbolp1 = symbolp1.upper()
    if symbolp1 == "X" :
      symbolp2 = "O"
      print(f"\nPlayer1 plays as {symbolp1}")
      print(f"Player2 plays as {symbolp2}")
      unvalid_symbol = False
    elif symbolp1 == "O" :
      symbolp2 = "X"
      print(f"\nPlayer1 plays as {symbolp1}")
      print(f"Player2 plays as {symbolp2}")
      unvalid_symbol = False
    else :
      print("Unvalid input")
  
  
  while nowin == True and nodraw == True:
    call = ""
    
    print(f"Round: {rounds}")
    print_board()
    if rounds % 2 == 0:
      if minirounds % 2 != 0:
        print("-- Player1 --")
        while unvaldicall == True:
          call = input("Where do you wanna place: ")
          check_valid_p1(call)
      else:
        print("-- Player2 --")
        while unvaldicall == True:
          call = input("Where do you wanna place: ")
          check_valid_p2(call)
    else:
      if minirounds % 2 == 0:
        print("-- Player1 --")
        while unvaldicall == True:
          call = input("Where do you wanna place: ")
          check_valid_p1(call)
      else:
        print("-- Player2 --")
        while unvaldicall == True:
          call = input("Where do you wanna place: ")
          check_valid_p2(call)
    


    
    
    winner = check_winner()
    if winner:
        print(f"SPieler {winner} hat gewonnen")
    
    
    
    unvaldicall = True
    minirounds = minirounds + 1
    weiter = input("Next round")
    if weiter == "end":
      nowin = False
    elif weiter == "nextr":
      rounds = rounds + 1
      minirounds = 0
    
  print("Match over")