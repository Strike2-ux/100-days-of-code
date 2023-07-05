import random
print("Dado infinito 🎲")
  
sides = int(input("¿Cuantos lados tiene tú dado?: "))
playGame = "yes"
  
def rollDice(sides):
  print("Lanzaste ", random.randint(1,sides))
while playGame == "yes":
    rollDice(sides)
    playGame = input("¿Lanzar otra vez?")