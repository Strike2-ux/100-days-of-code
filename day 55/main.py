import os, time, random

# Inicializar la lista de tareas y verificar si el archivo existe
tareas = []
archivoExiste = True
try:
    archivo = open("tareas_por_hacer.txt", "r")
    tareas = eval(archivo.read())
    archivo.close()
except:
    archivoExiste = False

def agregar_tarea():
    time.sleep(1)
    os.system("clear")
    nombre = input("Nombre > ")
    fecha = input("Fecha de vencimiento > ")
    prioridad = input("Prioridad > ").capitalize()
    fila = [nombre, fecha, prioridad]
    tareas.append(fila)
    print("Tarea agregada")

def ver_tareas():
    time.sleep(1)
    os.system("clear")
    opcion = input("1: Todas\n2: Por Prioridad\n> ")
    if opcion == "1":
        for fila in tareas:
            for elemento in fila:
                print(elemento, end=" | ")
            print()
        print()
    else:
        prioridad = input("¿Qué prioridad? > ").capitalize()
        for fila in tareas:
            if prioridad in fila:
                for elemento in fila:
                    print(elemento, end=" | ")
                print()
        print()
    time.sleep(1)

def editar_tarea():
    time.sleep(1)
    os.system("clear")
    buscar = input("Nombre de la tarea a editar > ")
    encontrada = False
    for fila in tareas:
        if buscar in fila:
            encontrada = True
    if not encontrada:
        print("No se encontró esa tarea")
        return
    for fila in tareas:
        if buscar in fila:
            tareas.remove(fila)
    nombre = input("Nombre > ")
    fecha = input("Fecha de vencimiento > ")
    prioridad = input("Prioridad > ").capitalize()
    fila = [nombre, fecha, prioridad]
    tareas.append(fila)
    print("Tarea agregada")

def eliminar_tarea():
    time.sleep(1)
    os.system("clear")
    buscar = input("Nombre de la tarea a eliminar > ")
    for fila in tareas:
        if buscar in fila:
            tareas.remove(fila)

while True:
    menu = input("1: Agregar\n2: Ver\n3: Editar\n4: Eliminar\n> ")
    if menu == "1":
        agregar_tarea()
    elif menu == "2":
        ver_tareas()
    elif menu == "3":
        editar_tarea()
    else:
        eliminar_tarea()

    time.sleep(1)
    os.system("clear")

    if archivoExiste:
        try:
            os.mkdir("respaldos")
        except:
            pass
        nombre_respaldo = f"respaldo{random.randint(1,1000000000)}.txt"
        os.popen(f"cp tareas_por_hacer.txt respaldos/{nombre_respaldo}")

    archivo = open("tareas_por_hacer.txt", "w")
    archivo.write(str(tareas))
    archivo.close()

'''
import os, time, random, json

tareas = []
archivoExiste = os.path.isfile("tareas_por_hacer.json")

def agregar_tarea():
    time.sleep(1)
    os.system("clear")
    nombre = input("Nombre > ")
    fecha = input("Fecha de vencimiento > ")
    prioridad = input("Prioridad > ").capitalize()
    fila = [nombre, fecha, prioridad]
    tareas.append(fila)
    print("Tarea agregada")

def ver_tareas():
    time.sleep(1)
    os.system("clear")
    opcion = input("1: Todas\n2: Por Prioridad\n> ")
    if opcion == "1":
        for fila in tareas:
            for elemento in fila:
                print(elemento, end=" | ")
            print()
        print()
    else:
        prioridad = input("¿Qué prioridad? > ").capitalize()
        for fila in tareas:
            if prioridad in fila:
                for elemento in fila:
                    print(elemento, end=" | ")
                print()
        print()
    time.sleep(1)

def editar_tarea():
    time.sleep(1)
    os.system("clear")
    buscar = input("Nombre de la tarea a editar > ")
    encontrada = False
    for fila in tareas:
        if buscar in fila:
            encontrada = True
    if not encontrada:
        print("No se encontró esa tarea")
        return
    tareas[:] = [fila for fila in tareas if buscar not in fila]
    nombre = input("Nombre > ")
    fecha = input("Fecha de vencimiento > ")
    prioridad = input("Prioridad > ").capitalize()
    fila = [nombre, fecha, prioridad]
    tareas.append(fila)
    print("Tarea agregada")

def eliminar_tarea():
    time.sleep(1)
    os.system("clear")
    buscar = input("Nombre de la tarea a eliminar > ")
    tareas[:] = [fila for fila in tareas if buscar not in fila]

while True:
    menu = input("1: Agregar\n2: Ver\n3: Editar\n4: Eliminar\n> ")
    if menu == "1":
        agregar_tarea()
    elif menu == "2":
        ver_tareas()
    elif menu == "3":
        editar_tarea()
    else:
        eliminar_tarea()

    time.sleep(1)
    os.system("clear")

    if archivoExiste:
        try:
            os.mkdir("respaldos")
        except:
            pass
        nombre_respaldo = f"respaldo{random.randint(1,1000000000)}.json"
        with open(nombre_respaldo, "w") as respaldo:
            json.dump(tareas, respaldo)

    with open("tareas_por_hacer.json", "w") as archivo:
        json.dump(tareas, archivo)

'''