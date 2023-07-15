def newPrint(color, word):
  if color=="rojo":
    print("\033[31m", word, sep="", end="")
  elif color=="verde":
    print("\033[32m", word, sep="", end="")
  elif color=="azul":
    print("\033[34m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")

print("Super Subroutine")
print("With my ", end="")
newPrint("rojo", "new program")
newPrint("reset", " I can just call rojo('and') ")
newPrint("rojo", "it will print in rojo ")
newPrint("azul", "or even blue")