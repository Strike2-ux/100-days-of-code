"""def print_list(rolodex):
    print()
    for name in rolodex:
        print(name)
    print()

def get_name():
    while True:
        first_name = input("First Name: ").strip().capitalize()
        last_name = input("Last Name: ").strip().capitalize()
        if not first_name or not last_name:
            print("ERROR: First name and last name must not be empty.")
        else:
            return f"{first_name} {last_name}"

def main():
    rolodex = set()

    while True:
        name = get_name()
        if name in rolodex:
            print("ERROR: Duplicate name")
        else:
            rolodex.add(name)
            print_list(rolodex)

        choice = input("Do you want to add another name? (yes/no): ").lower()
        if choice != "yes":
            break

if __name__ == "__main__":
    main()
"""

vueltadres = []

def printList():
  print()
  for name in vueltadres:
    print(name)
  print()

while True:
  firstName = input("First Name: ").strip().capitalize()
  lastName = input("Last Name: ").strip().capitalize()
  name = f"{firstName} {lastName}"
  if name not in vueltadres:
    vueltadres.append(name)
  else:
    print("ERROR: Duplicate name")
  printList()