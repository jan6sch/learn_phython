username = str(input("Enter your name here --> "))

leangth = len(username)
digits = username.isalpha()

if leangth > 12:
  print("Username to long, max 12 characters")
elif digits == False:
  print("No digits and spaces")
else:
  print("Your username is valid")