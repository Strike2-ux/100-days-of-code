exit = "no"


while exit == "no":
  animal_sound = input("What animal sound do you want to hear?").upper()
  
  if animal_sound == "COW":
    print("🐮 Moo")
  elif animal_sound == "PIG":
    print ("🐷 Oink")
  elif animal_sound == "SHEEP":
    print ("🐑 Baaa")
  elif animal_sound == "DUCK":
    print("🦆 Quack")
  elif animal_sound == "DOG":
    print("🐶 Woof")
  elif animal_sound == "CAT":
    print("🐱 Meow")
  else: 
    print("I don't know that animal sound. Try again.")


  exit = input("Do you want to exit?: ")