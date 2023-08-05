import os
import time

mokedex = {}

def prettyPrint():
  print(f"Nombre\tTipo\tHP\tMP")
  for key, value in mokedex.items():
    print(f"""{key:^12}|{value["tipo"]:^10}|{value["hp"]:^6}|{value["mp"]:^6}""")

while True:
  print("¡Agrega a tu Bestia!")
  nombre = input("Nombre > ").title()
  tipo = input("Tipo > ").title()
  hp = int(input("HP > "))
  mp = int(input("MP > "))
  mokedex[nombre] = { "tipo": tipo, "hp": hp, "mp": mp}
  print("----------")
  print()
  prettyPrint()
'''
import os, time

mokedex = {}

def prettyPrint():
  print(f"Name\tType\tHP\tMP")
  for key, value in mokedex.items():
    print(f"""{key:^12}|{value["type"]:^10}|{value["hp"]:^6}|{value["mp"]:^6}""")

while True:
  print("Add your Beast!")
  name = input("Name > ").title()
  type = input("Type > ").title()
  hp = int(input("HP > "))
  mp = int(input("MP > "))
  mokedex[name] = { "type": type, "hp": hp, "mp": mp}
  print("----------")
  print()
  prettyPrint()
'''