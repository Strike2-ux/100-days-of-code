'''import os, time
pizza = []

try:
  f = open("pizza.txt", "r")
  pizza = eval(f.read())
  f.close()
except:
  print("ERROR: No exist una lista de pizzas, en blanco la lista")

def verPizza():
  h1 = "Name"
  h2 = "Topping"
  h3 = "Size"
  h4 = "Quantity"
  h5 = "Total"
  print(f"{h1:^10}{h2:^20}{h3:^10}{h4:^10}{h5:^10}")
  for row in pizza:
    print(f"{row[0]:^10}{row[1]:^20}{row[2]:^10}{row[3]:^10}{row[4]:^10}")
  time.sleep(2)

def agregarPizza():
  time.sleep(1)
  os.system("clear")
  name = input("Nombre: ")
  toppings = input("Ingredientes: ")
  size = input("Tamaño (s/m/l): ").lower()
  while True:
    try:
      qty = int(input("Cantidad: "))
      break
    except:
      print("Error: La cantidad debe ser un numero")
  cost = 0
  if size=="s":
    cost = 5.99
  elif size=="m":
    cost = 9.99
  else:
    cost = 14.99
  total = cost * qty
  total = round(total, 2)
  row = [name, toppings, size, qty, total]
  pizza.append(row)

while True:
  time.sleep(1)
  os.system("clear")
  print("Dominos Pizza")
  print()
  menu = input("1: Agregar Pizza\n2: Ver Pizzas\n> ")
  if menu == "1":
    agregarPizza()
  else:
    verPizza()
  f = open("pizza.txt", "w")
  f.write(str(pizza))
  f.close()
  '''

import os
import time

def load_pizzas():
    try:
        with open("pizza.txt", "r") as f:
            pizza_data = f.read()
            if pizza_data:
                return eval(pizza_data)
    except (FileNotFoundError, SyntaxError):
        print("No existe una lista de pizzas o está vacía.")
    return []

def save_pizzas(pizza_list):
    with open("pizza.txt", "w") as f:
        f.write(str(pizza_list))

def display_pizzas(pizza_list):
    h1, h2, h3, h4, h5 = "Name", "Topping", "Size", "Quantity", "Total"
    print(f"{h1:^10}{h2:^20}{h3:^10}{h4:^10}{h5:^10}")
    for row in pizza_list:
        print(f"{row[0]:^10}{row[1]:^20}{row[2]:^10}{row[3]:^10}{row[4]:^10}")
    time.sleep(2)

def add_pizza(pizza_list):
    os.system("clear")
    name = input("Nombre: ")
    toppings = input("Ingredientes: ")
    size = input("Tamaño (s/m/l): ").lower()
    while True:
        try:
            qty = int(input("Cantidad: "))
            break
        except ValueError:
            print("Error: La cantidad debe ser un número.")
    cost = 0
    if size == "s":
        cost = 5.99
    elif size == "m":
        cost = 9.99
    else:
        cost = 14.99
    total = round(cost * qty, 2)
    row = [name, toppings, size, qty, total]
    pizza_list.append(row)

def main():
    pizza = load_pizzas()

    while True:
        os.system("clear")
        print("Dominos Pizza")
        print()
        menu = input("1: Agregar Pizza\n2: Ver Pizzas\n3: Salir\n> ")

        if menu == "1":
            add_pizza(pizza)
        elif menu == "2":
            display_pizzas(pizza)
        elif menu == "3":
            save_pizzas(pizza)
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
