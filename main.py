import random

def diceRoll(quantity, diceSize):
  cont = 0
  result = 0 
  while (cont < quantity):
    value = random.randint(1, diceSize)
    print(value)
    result += value
    cont+= 1
  print(result)

diceRoll(1, 10)