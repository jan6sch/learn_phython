import random
play = str(input("Do you wanna play? Y/N: "))
while play == "Y":
  play = "N"
  random_number = random.randint(1, 100)
  print("You have 5 trys to guess the random number between 1 and 100")

  trys = 5

  while trys != 0:
    guess = int(input("Guess a number: "))

    if random_number == guess:
      print(f"Your correct, the random number was {random_number}")
      trys = 0
    elif random_number > guess:
      print(f"{guess} is not the right number. The random number is higher than {guess}")
      trys = trys - 1
      print(f"You have {trys} trys left")
    elif random_number < guess:
      print(f"{guess} is not the right number. The random number is lower than {guess}")
      trys = trys - 1
      print(f"You have {trys} trys left")
    
  if random_number != guess:
    print(f"You have no more trys left, the random number was {random_number}")
  else:
    print("finish")
  play = str(input("Do you wanne play again? Y/N: "))

print("Okay bye")

