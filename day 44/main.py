'''import random, os, time

bingo = []

def ran():
  number = random.randint(1,90)
  return number

def prettyPrint():
  for row in bingo:
    for item in row:
      print(item, end="\t|\t")
    print()

def createCard():
  global bingo
  numbers = []
  for i in range(8):
    num = ran()
    while num in numbers:
      num = ran()
    numbers.append(ran())
  
  numbers.sort()
  
  bingo = [ [ numbers[0], numbers[1], numbers[2]],
            [ numbers[3], "BG", numbers[4] ],
            [ numbers [5], numbers[6], numbers[7]]
          ]

createCard()
while True:
  prettyPrint()
  num = int(input("Next Number: "))
  for row in range(3):
    for item in range(3):
      if bingo[row][item] == num:
        bingo[row][item] = "X"

  exes = 0
  for row in bingo:
    for item in row:
      if item=="X":
        exes+=1

  if exes == 8:
    print("You have won")
    break

  time.sleep(1)
  os.system("clear")'''

import random

def obtener_entrada_usuario():
    while True:
        try:
            numeros = input("Ingrese 8 números únicos entre 1 y 90, separados por espacios: ")
            numeros = list(map(int, numeros.split()))
            if len(numeros) != 8 or any(num < 1 or num > 90 for num in numeros) or len(numeros) != len(set(numeros)):
                raise ValueError
            return numeros
        except ValueError:
            print("Entrada inválida. Por favor, ingrese 8 números únicos entre 1 y 90.")

def generar_numeros_aleatorios():
    return random.sample(range(1, 91), 8)

def comprobar_y_reemplazar_duplicados(numeros):
    while len(numeros) != len(set(numeros)):
        numeros = generar_numeros_aleatorios()
    return numeros

def crear_tablero_bingo():
    opcion = input("¿Desea ingresar sus propios números? (S/N): ")
    if opcion.lower() == 's':
        numeros = obtener_entrada_usuario()
    else:
        numeros = comprobar_y_reemplazar_duplicados(generar_numeros_aleatorios())

    numeros.sort()
    tablero_bingo = {
        'B': [numeros[0], numeros[1], numeros[2]],
        'I': [numeros[3], "BINGO", numeros[4]],
        'N': [numeros[5], numeros[6], numeros[7]],
    }
    return tablero_bingo

def imprimir_tablero_bingo(tablero_bingo):
    print("Tablero de Bingo:")
    for letra, numeros in tablero_bingo.items():
        print(f'{letra:<3}', end='')
        print(' '.join(f'{str(num):<3}' for num in numeros))

tablero_bingo = crear_tablero_bingo()
imprimir_tablero_bingo(tablero_bingo)


#the important it's to understand the structure of the defnitions 