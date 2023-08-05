ElpokedexdePaulex = {"Beast Name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}

print("ElpokedexdePaulex")
print()

for name, value in ElpokedexdePaulex.items():
  ElpokedexdePaulex[name] = input(f"{name}:\t").strip().title()

if ElpokedexdePaulex["Type"]=="Earth":
  print("\033[32m", end="")
elif ElpokedexdePaulex["Type"]=="Air":
  print("\033[37m", end="")
elif ElpokedexdePaulex["Type"]=="Fire":
  print("\033[31m", end="")
elif ElpokedexdePaulex["Type"]=="Water":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")

for name, value in ElpokedexdePaulex.items():
  print(f"{name:<15}: {value}")