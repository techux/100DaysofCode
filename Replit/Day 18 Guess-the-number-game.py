# Day 18 Guess the number game in python Completed

import random

print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")

correct_number = random.randrange(1,1000000)
attempt = 1
print(correct_number)
while True:
  user_guess = int(input("Pick a number between 1 and 1,000,000: "))
  if user_guess < 0:
    print("You entered below or equal to 0. Try Greater than 1")
    exit()
  if user_guess < correct_number:
    print("That number is low. Try again!")
    attempt += 1
  elif user_guess > correct_number:
    print("That number is high. Try again!")
    attempt += 1
  elif user_guess == correct_number:
    print(f"You are a winner! Took {attempt} count to guess")
    break 
  else:
    print("That is not a number I recognize.")
