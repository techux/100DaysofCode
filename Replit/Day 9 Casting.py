# Day 9 of 100 Days of Python on Replit

birthyear = input('In what year were you born? ')
birthyear = int(birthyear)
if birthyear >= 1925 and birthyear <=	1946: 
  print('You are a Traditionalist.')
elif birthyear >= 1947 and birthyear <=	1964: 
  print('You are a Baby Boomer.')
elif birthyear >= 1965 and birthyear <=	1981: 
  print('You belonng to Gen X.')
elif birthyear >= 1982 and birthyear <=	1995: 
  print('You are a Millenial.')
elif birthyear >= 1996 and birthyear <=	2015: 
  print('You belong to Gen Z.')
else:
  print('You are either very old or very young.')