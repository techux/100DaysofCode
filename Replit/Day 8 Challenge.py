# Day 8 of 100 days of python Completed
username = input("What is your name?: ")
if username == 'Klaus' or username == 'klaus':
  dayofweek = input("What is the current day of the week?: ")
  favlanguage = input("What is your favourite programming language?: ")
  favbeverage = input("What is your favourite beverage?: ")
  print(f'Hello {username}! It is a beautiful {dayofweek}. \nI wish you a lot of fun and success while coding in {favlanguage}. Don\'t work too much. And when you\'re done enjoy your {favbeverage}. \nYou totally earned it mate!')

elif username == 'Dev' or username == 'dev':
  print(f'Hello {username}! You\'re a knob!')
else:
  print(f'Hello {username}! We haven\'t met before, have we?\nHave a lovely day!')