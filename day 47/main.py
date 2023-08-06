
'''import os, time, random

triunfadores = {}
triunfadores["david"] = {"Inteligencia": 178, "Velocidad": 4, "Engaño": 80, "Nivel de pelada": 99}
triunfadores["mr spock"] = {"Inteligencia": 200, "Velocidad": 50, "Engaño": 50, "Nivel de pelada": 0}
triunfadores["moica from friends"] = {"Inteligencia": 150, "Velocidad": 50, "Engaño": 50, "Nivel de pelada": 0}
triunfadores["professor x"] = {"Inteligencia": 250, "Velocidad": 1, "Engaño": 200, "Nivel de pelada": 101}

while True:
  print("El TOP de triunfadores")
  print()
  print("Personajes")
  print()
  for key in triunfadores:
    print(key)
  user = input("ELije tu personaje\n> ").lower()
  comp = random.choice(list(triunfadores.keys()))
  print("Computadora a elegido", comp)

  print("Elija sus estadisticas: Inteligencia, Velocidad, Engaño & Nivel de pelada")

  answer = input("> ")

  print(f"{user}: {triunfadores[user][answer]}")
  print(f"{comp}: {triunfadores[comp][answer]}")

  if triunfadores[user][answer] > triunfadores[comp][answer]:
    print(user, "Ganó")
  elif triunfadores[user][answer] < triunfadores[comp][answer]:
    print(comp, "Ganó")
  else:
    print("Empate")


  time.sleep(2)
  os.system("clear")
  '''

import os
import time
import random

triunfadores = {
    "david": {"inteligencia": 178, "velocidad": 4, "engaño": 80, "nivel de pelada": 99},
    "mr spock": {"inteligencia": 200, "velocidad": 50, "engaño": 50, "nivel de pelada": 0},
    "moica from friends": {"inteligencia": 150, "velocidad": 50, "engaño": 50, "nivel de pelada": 0},
    "professor x": {"inteligencia": 250, "velocidad": 1, "engaño": 200, "nivel de pelada": 101}
}

def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print("Opción no válida. Por favor, elige una opción válida.")

def get_valid_stat_input():
    valid_stats = ["inteligencia", "velocidad", "engaño", "nivel de pelada"]
    return get_valid_input("Elige tus estadísticas: Inteligencia, Velocidad, Engaño y Nivel de pelada\n> ", valid_stats)

def print_character_stats(character):
    for stat, value in triunfadores[character].items():
        print(f"{stat}: {value}")

while True:
    print("El TOP de triunfadores")
    print()
    print("Personajes")
    print()
    for key in triunfadores:
        print(key)
    user = get_valid_input("Elige tu personaje\n> ", triunfadores.keys())
    comp = random.choice(list(triunfadores.keys()))
    print("Computadora ha elegido", comp)

    answer = get_valid_stat_input()

    print_character_stats(user)
    print_character_stats(comp)

    user_stat_value = triunfadores[user][answer.lower()]
    comp_stat_value = triunfadores[comp][answer.lower()]

    if user_stat_value > comp_stat_value:
        print(user.capitalize(), "Ganó")
    elif user_stat_value < comp_stat_value:
        print(comp.capitalize(), "Ganó")
    else:
        print("Empate")

    time.sleep(2)
    os.system("clear")