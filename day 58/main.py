''' <!----brokencode---->
import random, os, time
totalAttempts = 0

def game():
  attempts = 0
  while True:
    number = random.randint(1,100)
    guess = int(input("Pick a number between 1 and 100: "))
    if guess > number:
      print("Too high")
      attempts+=1
    elif guess < number:
      print("Too low")
      attempts+=1
    else:
      print("Just right!")
      print(f"{attempts} attempts this round")
      return attempts

while True:
  menu = input("1: Guess the random number game\n2: Total Score\n3: Exit\n> ")
  if menu == 1:
    totalAttempts+= game()
  elif menu == 2:
    print(f"You've had {totalAttempts} attempts")
  else:
    break
'''

import random, os, time
totalAttempts = 0

def game():
  attempts = 0
  number = random.randint(1,100)
  while True:
    guess = int(input("Elije un número del 1 al 100: "))
    if guess > number:
      print("Demasiado Alto")
      attempts+=1
    elif guess < number:
      print("Demasiado bajo")
      attempts+=1
    else:
      print("Correcto!")
      print(f"{attempts} intentos en esta ronda")
      return attempts

while True:
  menu = int(input("1: Adivina un numero al azar\n2: Puntaje todal\n3: Salir\n> "))
  if menu == 1:
    totalAttempts+= game()
  elif menu == 2:
    print(f"Tu tienes {totalAttempts} intentos")
  else:
    break
  

import random
'''
# Constants
MIN_NUMBER = 1
MAX_NUMBER = 100

totalAttempts = 0

def game():
    attempts = 0
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    while True:
        guess = int(input(f"Elije un número del {MIN_NUMBER} al {MAX_NUMBER}: "))
        attempts += 1
        if guess > number:
            print("Demasiado Alto")
        elif guess < number:
            print("Demasiado bajo")
        else:
            print("Correcto!")
            print(f"{attempts} intentos en esta ronda")
            return attempts

while True:
    menu = int(input("1: Adivina un numero al azar\n2: Puntaje todal\n3: Salir\n> "))
    if menu == 1:
        totalAttempts += game()
    elif menu == 2:
        print(f"Tu tienes {totalAttempts} intentos")
    else:
        break
'''
'''
import random

def game():
  number = random.randint(1, 100)
  attempts = 0
  while attempts <= 10:
    guess = int(input("Pick a number between 1 and 100: "))
    if guess > number:
      print("Too high")
    elif guess < number:
      print("Too low")
    else:
      print("Just right!")
      return attempts
    attempts += 1
  print("You lose! The number was", number)
  return attempts

def main():
  total_attempts = 0
  while True:
    menu = int(input("1: Play\n2: Show total attempts\n3: Quit\n> "))
    if menu == 1:
      total_attempts += game()
    elif menu == 2:
      print("Total attempts:", total_attempts)
    elif menu == 3:
      break

if __name__ == "__main__":
  main()


'''