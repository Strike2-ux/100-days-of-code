'''import os, time
inventory = []

try:
  f = open("inventory.txt", "r")
  inventory = eval(f.read())
  f.close()
except:
  pass

def addItem():
  time.sleep(1)
  os.system("clear")
  print("INVENTORY")
  print("=========")
  print()
  item = input("Item to add > ").capitalize()
  inventory.append(item)
  print("Added")

def viewItem():
  time.sleep(1)
  os.system("clear")
  print("INVENTORY")
  print("=========")
  print()
  seen = []
  for item in inventory:
    if item not in seen:
      print(f"{item} {inventory.count(item)}")
      seen.append(item)

  time.sleep(2)

def removeItem():
  time.sleep(1)
  os.system("clear")
  print("INVENTORY")
  print("=========")
  print()
  item = input("Item to remove > ").capitalize()
  if item in inventory:
    inventory.remove(item)
    print("Removed")
  else:
    print("You don't have that item")


while True:
  time.sleep(1)
  os.system("clear")
  print("INVENTORY")
  print("=========")
  print()
  menu = input("1: Add\n2: View\n3: Remove\n> ")
  if menu=="1":
    addItem()
  elif menu=="2":
    viewItem()
  else:
    removeItem()

  f = open("inventory.txt", "w")
  f.write(str(inventory))
  f.close()'''

import os
import time

# Load inventory from file
def load_inventory():
    try:
        with open("inventory.txt", "r") as f:
            return eval(f.read())
    except (FileNotFoundError, SyntaxError):
        return []

# Save inventory to file
def save_inventory(inventory):
    with open("inventory.txt", "w") as f:
        f.write(str(inventory))

def add_item(inventory):
    os.system("clear")
    print("INVENTORY")
    print("=========")
    print()
    item = input("Item to add > ").strip().capitalize()
    if item:
        inventory[item] = inventory.get(item, 0) + 1
        print("Added")
    else:
        print("Invalid input")

def view_items(inventory):
    os.system("clear")
    print("INVENTORY")
    print("=========")
    print()
    for item, count in inventory.items():
        print(f"{item} {count}")
    time.sleep(2)

def remove_item(inventory):
    os.system("clear")
    print("INVENTORY")
    print("=========")
    print()
    item = input("Item to remove > ").strip().capitalize()
    if item in inventory:
        if inventory[item] > 1:
            inventory[item] -= 1
        else:
            del inventory[item]
        print("Removed")
    else:
        print("Item not found in inventory")

def main():
    inventory = load_inventory()

    while True:
        os.system("clear")
        print("INVENTORY")
        print("=========")
        print()
        print("1: Add\n2: View\n3: Remove\n4: Quit")
        menu = input("> ").strip()

        if menu == "1":
            add_item(inventory)
        elif menu == "2":
            view_items(inventory)
        elif menu == "3":
            remove_item(inventory)
        elif menu == "4":
            break
        else:
            print("Invalid choice")

        save_inventory(inventory)

if __name__ == "__main__":
    main()
