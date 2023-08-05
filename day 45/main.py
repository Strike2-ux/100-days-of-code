'''# | Name | Date | Priority
import os, time
todo = []

def add():
  time.sleep(1)
  os.system("clear")
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def view():
  time.sleep(1)
  os.system("clear")
  options = input("1: All\n2: By Priority\n> ")
  if options=="1":
    for row in todo:
      for item in row:
        print(item, end=" | ")
      print()
    print()
  else:
    priority = input("What priority? > ").capitalize()
    for row in todo:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    print()
  time.sleep(1)

def edit():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to edit > ")
  found = False
  for row in todo:
    if find in row:
      found = True
  if not found:
    print("Couldn't find that")
    return
  for row in todo:
    if find in row:
      todo.remove(row)
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def remove():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to remove > ")
  for row in todo:
    if find in row:
      todo.remove(row)

while True:
  menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  else:
    remove()

  time.sleep(1)
  os.system("clear")'''
def agregar_persona(data, nombre, edad, ocupacion):
    data[nombre] = {'edad': edad, 'ocupacion': ocupacion}

def editar_persona(data, nombre, nueva_edad, nueva_ocupacion):
    if nombre in data:
        data[nombre]['edad'] = nueva_edad
        data[nombre]['ocupacion'] = nueva_ocupacion
    else:
        print(f"{nombre} no se encontró en el diccionario.")

def ver_personas(data):
    for nombre, info in data.items():
        print(f"Nombre: {nombre}, Edad: {info['edad']}, Ocupación: {info['ocupacion']}")

if __name__ == "__main__":
    datos_personas = {}

    while True:
        print("\n1. Agregar persona\n2. Editar usuario\n3. Ver todas las personas\n4. Salir")
        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            nombre = input("Ingrese el nombre de la persona: ")
            edad = int(input("Ingrese la edad de la persona: "))
            ocupacion = input("Ingrese la ocupación de la persona: ")
            agregar_persona(datos_personas, nombre, edad, ocupacion)

        elif opcion == 2:
            nombre = input("Ingrese el nombre de la persona para editar: ")
            nueva_edad = int(input("Ingrese la nueva edad: "))
            nueva_ocupacion = input("Ingrese la nueva ocupación: ")
            editar_persona(datos_personas, nombre, nueva_edad, nueva_ocupacion)

        elif opcion == 3:
            ver_personas(datos_personas)

        elif opcion == 4:
            break

        else:
            print("¡Opción inválida! Por favor, intente nuevamente.")
