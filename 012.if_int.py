age = int(input("How old are you?: "))

if age >= 18:
  print("You are above 18!")
elif age <= 0:
  print("Incorrect input! Try again")
else:
  print("You are below 18!")