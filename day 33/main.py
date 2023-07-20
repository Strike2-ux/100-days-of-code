'''myPartyList = []

def printList():
  print() 
  for item in myPartyList:
    print(item)
  print() 

while True:
  menu = input("add or remove?: ").lower()
  if menu == "add":
    item = input("Who should I add to the party list?: ")
    myPartyList.append(item)
  elif menu == "remove":
    item = input("Who should I remove from the party list?: ")
    if item in myPartyList:
      myPartyList.remove(item)
    else:
      print(f"{item} was not in the list")
  printList() '''


import os, time
toDoList = []

def printList():
  print()
  for item in toDoList:
    print(item)
  print()

while True:
  menu = input("ToDoList Manager\n\nDo you want to view, add or edit the todo list?\n").lower()
  if menu=="view":
    printList()
  elif menu=="add":
    item = input("What do you want to add?\n")
    toDoList.append(item)
  elif menu=="edit":
    item = input("What do you want to remove?\n")
    if item in toDoList:
      toDoList.remove(item)
    else:
      print(f"{item} was not in the list")

