'''import os, time

f = open("high.score", "r")
scores = f.read().split("\n")
f.close()

highscore = 0
name = None

for rows in scores:
  data = rows.split()
  if data != []:
    if int(data[1]) > highscore:
      highscore = int(data[1])
      name = data[0]

print("The winner is", name, "with", highscore)'''

# Utilizar la declaración "with" para cerrar automáticamente el archivo
with open("high.score", "r") as f:
    scores = f.read().split("\n")

highscore = 0
nombre = None

# Iterar a través de cada fila en la lista de puntajes
for fila in scores:
    data = fila.split()
    
    # Saltar líneas vacías
    if not data:
        continue
    
    # Asegurarse de que la fila tenga al menos dos elementos antes de intentar acceder a ellos
    if len(data) >= 2:
        nombre_jugador = data[0]
        puntaje_jugador = int(data[1])
        
        # Actualizar el puntaje más alto y el nombre si es necesario
        if puntaje_jugador > highscore:
            highscore = puntaje_jugador
            nombre = nombre_jugador

# Manejar el caso en que no se encontraron puntajes altos
if nombre is not None:
    print("El ganador es", nombre, "con un puntaje alto de", highscore)
else:
    print("No se encontraron puntajes altos.")
