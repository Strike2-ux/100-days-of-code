import os, time

while True:
  print("HIGH SCORE TABLE")
  print()
  name = input("INITIALS > ").upper()
  score = input("SCORE > ")
  print()

  f = open("maximo.puntaje", "a+")
  f.write(f"{name} {score}\n")
  f.close()

  print("AGREGADO")
  time.sleep(1)
  os.system("clear")