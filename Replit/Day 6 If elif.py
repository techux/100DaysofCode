# Day 6 of Python - If elif else

username = input('Username > ')
password = input('Password > ')
if username == 'devesh' and password == 'devesh1234':
  print(f'Welcome back, Mr {username}!')
elif username == 'admin' and password == 'Admin@12345':
  print('Welcome back, Admin!')
elif username == 'rajat' and password == 'MyPassword':
  print('Welcome back, Rajat!')
else:
  print('No way!')
