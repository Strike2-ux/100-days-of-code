print("Bienvenido a las canciones")
print()
print("Averigua la siguiente palabra: payaso \U0001F921")
print()

contador = 1
while True:
    canciones = input("I  ______ a thing. ")
    if canciones == "miss" or canciones == "Miss":
        print("¡Correcto!")
        break
    elif contador == 3:
        print("¡Oh no! Has agotado todos tus intentos.")
        break
    else:
        print("¡Incorrecto! Inténtalo de nuevo.")
        contador += 1

print("¡Gracias por jugar!")
if contador > 1:
    print("Obtuviste la letra correcta en", contador, "intentos.")
else:
    print("Obtuviste la letra correcta en", contador, "intento.")