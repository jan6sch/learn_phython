import random

coin = ["heads", "tails"]

heads = 0
tails = 0
flip = 0
wflip = str(input("Wanne flip press enter: "))

if wflip == "" : 

  while wflip == "":
    wflip = 1
    result = random.choice(coin)
    print(result)
    if result == "heads":
      heads = heads + 1
    else:
      tails = tails + 1
    flip = flip + 1
    
    print(f"{heads} x H, {tails} x T, {flip} x fliped")

    wflip = str(input("Flip?"))

  print(f"Overall you had {heads} x H, {tails} x T, {flip} x fliped")
  heads_percent = (heads / flip) * 100
  tails_percent = (tails / flip) * 100

  print(f"{heads_percent}% H, {tails_percent}% T")
else : 
  print("Already finished?")