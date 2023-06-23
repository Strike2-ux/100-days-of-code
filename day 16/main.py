print("Bienvenido a las canciones")
print()
print("Averigua la siguiente palabra payaso \U0001F921")
print()

contador = 1
while True:
  canciones = input("I  ______ a thing. ")
  if canciones == "miss" or canciones == "Miss":
    print("You got it!")
  else:
    print("Nope! Try again!")
    contador +=1
  if canciones == "miss":
    break
print("Thanks for playing!")

print("You got the correct lyrics in", contador, "intento(s).")