# | Name | Date | Priority
'''import os, time
todo = []
f = open("to.do", "r")
todo = eval(f.read())
f.close()

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
  os.system("clear")
  f = open("to.do", "w")
  f.write(str(todo))
  f.close()


  '''


import os
import time

ARCHIVO_TODO = "por_hacer.txt"

def cargar_lista_tareas():
    try:
        with open(ARCHIVO_TODO, "r") as f:
            return eval(f.read())
    except FileNotFoundError:
        return []

def guardar_lista_tareas(lista_tareas):
    with open(ARCHIVO_TODO, "w") as f:
        f.write(str(lista_tareas))

def agregar_tarea(lista_tareas):
    os.system("clear")
    nombre = input("Nombre > ")
    fecha = input("Fecha de vencimiento > ")
    prioridad = input("Prioridad > ").capitalize()
    tarea = [nombre, fecha, prioridad]
    lista_tareas.append(tarea)
    print("Tarea agregada")

def ver_tareas(lista_tareas):
    os.system("clear")
    opciones = input("1: Todas\n2: Por prioridad\n> ")
    if opciones == "1":
        for tarea in lista_tareas:
            print(" | ".join(tarea))
    else:
        prioridad = input("¿Qué prioridad? > ").capitalize()
        for tarea in lista_tareas:
            if prioridad in tarea:
                print(" | ".join(tarea))
    time.sleep(1)

def editar_tarea(lista_tareas):
    os.system("clear")
    buscar = input("Nombre de la tarea a editar > ")
    encontrada = False
    for tarea in lista_tareas:
        if buscar in tarea:
            encontrada = True
            lista_tareas.remove(tarea)
    if not encontrada:
        print("No se encontró esa tarea")
        return
    nombre = input("Nombre > ")
    fecha = input("Fecha de vencimiento > ")
    prioridad = input("Prioridad > ").capitalize()
    tarea = [nombre, fecha, prioridad]
    lista_tareas.append(tarea)
    print("Tarea editada")

def eliminar_tarea(lista_tareas):
    os.system("clear")
    buscar = input("Nombre de la tarea a eliminar > ")
    for tarea in lista_tareas:
        if buscar in tarea:
            lista_tareas.remove(tarea)
            print("Tarea eliminada")
            return
    print("No se encontró esa tarea")

def main():
    lista_tareas = cargar_lista_tareas()
    while True:
        menu = input("1: Agregar\n2: Ver\n3: Editar\n4: Eliminar\n5: Salir\n> ")
        if menu == "1":
            agregar_tarea(lista_tareas)
        elif menu == "2":
            ver_tareas(lista_tareas)
        elif menu == "3":
            editar_tarea(lista_tareas)
        elif menu == "4":
            eliminar_tarea(lista_tareas)
        elif menu == "5":
            guardar_lista_tareas(lista_tareas)
            print("Saliendo...")
            break
        else:
            print("Opción inválida")
        time.sleep(1)
        os.system("clear")

if __name__ == "__main__":
    main()
