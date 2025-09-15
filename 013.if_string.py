food = input("Do you like pizza? Y/N: ")

if food == "Y":
  print("You have good Taste")
elif food == "N":
  diet = input("Are you on diet? Y/N: ")
  if diet == "Y":
    print("Good!")
  elif diet == "N":
    print("You have bad taste!")
  else:
      print("Incorrect input! Try again.")
else: 
  print("Incorrect input! Try again.")


