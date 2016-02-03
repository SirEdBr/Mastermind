from random import random

print("Welcome to Mastermind! This is a programme written in python 3.")
input()
print("If you do not know the rules to this game, look it up.")
input()

one = random.randint(1,6)
two= random.randint(1,6)
three = random.randint(1,6)
four= random.randint(1,6)

print("The computer has chosen four random numbers.")
print("Type the first number of your guess here:")
1guess1 = input()
print("Type the second number of your guess here:")
1guess2 = input()
print("Type the third number of your guess here:")
1guess3= input()
print("Type the fourth number of your guess here:")
1guess4 = input()

print()
print("Here are your guess ratings.")

if 1guess1 == one:
  print(black)
elif 1guess1 == two or 1guess1 == three or 1guess1 == four:
  print(white)
else:
  print("Nothing")
