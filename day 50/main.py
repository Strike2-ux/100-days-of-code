"""import os, time, random

def agregar():
  os.system("clear")
  idea = input("Idea > ")
  f = open("my.ideas", "a+")
  f.write(f"{idea}\n")
  f.close()
  time.sleep(1)
  os.system("clear")

def mostrar():
  os.system("clear")
  f = open("mis.ideas", "r")
  ideas = f.read().split("\n")
  f.close()
  ideas.remove("")
  idea = random.choice(ideas)
  print(idea)
  time.sleep(2)
  os.system("clear")

while True:
  menu = input("1: Agregar una idea\n2: Mostrar una idea random\n> ")
  if menu == "1":
    agregar()
  else:
    mostrar()"""

import os, random, time

def clear_screen():
    os.system("clear")

def add():
    clear_screen()
    idea = input("Idea > ")
    with open("my.ideas", "a") as f:
        f.write(f"{idea}\n")
    time.sleep(1)
    clear_screen()

def show():
    clear_screen()
    with open("my.ideas", "r") as f:
        ideas = [idea.strip() for idea in f if idea.strip()]
    if ideas:
        random_idea = random.choice(ideas)
        print(random_idea)
    else:
        print("No ideas found.")
    time.sleep(2)
    clear_screen()

while True:
    menu = input("1: Add idea\n2: Show a random idea\n> ")
    if menu == "1":
        add()
    else:
        show()
