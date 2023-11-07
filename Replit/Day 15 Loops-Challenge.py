# Day 15 Challenge on Loops Complete 

exit = "no"

while exit == "no":
  animal_sound = input("What animal sound do you want to hear?")

  if animal_sound.lower() == "cow" :
    print("Moo")
  elif animal_sound.lower() == "pig" :
    print ("Oink")
  elif animal_sound.lower() == "sheep" :
    print ("Baaa")
  elif animal_sound.lower() == "duck" :
    print("Quack")
  elif animal_sound.lower() == "dog" :
    print("Woof")
  elif animal_sound.lower() == "cat" :
    print("Meow")
  else: 
    print("I don't know that animal sound. Try again.")


  exit = input("Do you want to exit?: ")