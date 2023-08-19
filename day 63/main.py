'''import random
from PIL import Image, ImageDraw
import sqlite3

# Función para lanzar el dado
def lanzar_dado():
    return random.randint(1, 6)

# Competencia de Lanzamiento de Dados entre 2 jugadores
puntaje_jugador1 = lanzar_dado()
puntaje_jugador2 = lanzar_dado()

print("Jugador 1 lanzó:", puntaje_jugador1)
print("Jugador 2 lanzó:", puntaje_jugador2)

if puntaje_jugador1 > puntaje_jugador2:
    print("¡Jugador 1 gana!")
elif puntaje_jugador2 > puntaje_jugador1:
    print("¡Jugador 2 gana!")
else:
    print("¡Es un empate!")

# Aventura de RPG
def aventura_rpg():
    print("¡Estás embarcando en una aventura de RPG!")
    # Lógica de la aventura aquí

aventura_rpg()

# Subrutina para Dibujar Imágenes
def dibujar_imagen():
    imagen = Image.new("RGB", (200, 200), "white")
    dibujo = ImageDraw.Draw(imagen)
    dibujo.rectangle([(50, 50), (150, 150)], outline="blue", width=3)
    imagen.show()

dibujar_imagen()

# Agregar Tareas y Guardar en un Archivo de Base de Datos
def agregar_tarea(tarea, conexion_db):
    cursor = conexion_db.cursor()
    cursor.execute("INSERT INTO tareas (nombre_tarea) VALUES (?)", (tarea,))
    conexion_db.commit()
    print("Tarea agregada:", tarea)

conexion_db = sqlite3.connect("main.db")
conexion_db.execute("CREATE TABLE IF NOT EXISTS tareas (nombre_tarea TEXT)")
tarea = input("Ingresa una tarea para el día: ")
agregar_tarea(tarea, conexion_db)
conexion_db.close()
'''
#si le cuesta / if it's hard for you:

import random

# Function to roll a dice
def roll_dice():
  return random.randint(1, 6)

# Function to play a game of dice
def play_game():
  player_1_score = 0
  player_2_score = 0

  # Play 10 rounds
  for i in range(10):
    # Roll the dice for player 1
    player_1_roll = roll_dice()

    # Roll the dice for player 2
    player_2_roll = roll_dice()

    # Add the roll to the player's score
    player_1_score += player_1_roll
    player_2_score += player_2_roll

  # The player with the highest score wins
  if player_1_score > player_2_score:
    print("Player 1 wins!")
  elif player_2_score > player_1_score:
    print("Player 2 wins!")
  else:
    print("Tie!")

# Main function
if __name__ == "__main__":
  play_game()
