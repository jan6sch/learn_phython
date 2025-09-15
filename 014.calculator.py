operator = input("Choose an operator (+  -  *  /): ")

number1 = float(input("Enter a number: "))
number2 = float(input("Enter a second number: "))

if operator == "+":
  print(number1 + number2)
elif operator == "-":
  print(number1 - number2)
elif operator == "*":
  print(number1 * number2)
elif number1 != "0" and number2 != "0":
   if operator == "/":
     print(number1 / number2)
   else:
     print("Incorrect input")
else:
  print("Incorrect input")