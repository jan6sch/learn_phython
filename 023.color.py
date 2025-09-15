import random



give_variables = str(input("Type in at least 2 variables splited with an ',': "))
variables = give_variables.replace(" ", "")
variables_check = variables.count(",")
if variables_check <= 0:
  print("Even you have not used , or you have not enough variables.")
else:
  variables = variables.split(',')
  print(variables)

  rounds = int(input("For how many rounds you wanne calculate? "))

  start = input("Type start: ")

  if start == "start":

    counts = {var : 0 for var in variables}
    print("Good boy")
    played_rounds = 0

    while played_rounds != rounds:
      played_rounds = played_rounds + 1

      result = random.choice(variables)

      counts [result] += 1
    
    print("\n--- Ergebnisse ---")
    for var, count in counts.items():
      print(f"{var}: {count}")

    

  else:
    print("Fail")