# Day 16 Whie True Loop - Complete the lyrics game

print("Complete the lyrics : ")
print("niid churaai meri, kisane ooo sanam, ______\n")

count = 1
ans = input("Enter your answer : ")
while ans.lower() != "tune" :
  print("Try again")
  ans = input("Enter your answer : ")
  count += 1
  
print("You won the game : Took you " + str(count))