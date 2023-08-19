
import datetime

# Set the access password
contraseña = "mi_secreta_contraseña"

# Prompt the user to type in the password
def obtener_contraseña():
  contraseña = input("Enter the password: ")
  return contraseña

# Check if the password is correct
def mirar_contraseña(contraseña):
  if contraseña == obtener_contraseña():
    return True
  else:
    print("Incorrect password!")
    exit()

# Main menu
def principal_menu():
  print("1. Add entry")
  print("2. View entries")
  print("3. Exit")
  choice = input("Enter your choice: ")
  return choice

# Add entry
def agregar_entrada():
  entrada = input("Enter your entry: ")
  estampillatiempo = datetime.datetime.now()

  # Store the entry in the database with the timestamp as the key
  with open("diario.db", "a") as f:
    f.write(f"{estampillatiempo}:{entrada}\n")

# View entries
def view_entries():
  # Get all the entries from the database
  with open("diario.db", "r") as f:
    entries = f.readlines()

  # Display the previous (most recent) entry
  print(entries[-1])

  # Loop through the entries and allow the user to view previous entries
  for i in range(len(entries) - 1, -1, -1):
    print(entries[i])
    input("Press Enter to view the previous entry.")

# Start the program
def comienzo():
  # Check the password
  if mirar_contraseña():
    # Display the main menu
    while True:
      choice = principal_menu()

      # Add an entry
      if choice == "1":
        agregar_entrada()

      # View entries
      elif choice == "2":
        view_entries()

      # Exit the program
      elif choice == "3":
        exit()

  else:
    print("Incorrect password!")
    exit()

comienzo()
# no basta con copiar y pegar, entienda el código, despliege y grabe en las bases de datos / copy and paste is not enough, understand the code, deploy and save in databases good.

'''
import datetime

# Set the access password
password = "secretpassword"

# Initialize an empty list to store diary entries
diary_entries = []

# Function to add an entry to the diary
def add_entry():
    entry = input("Type your entry: ")
    timestamp = datetime.datetime.now()
    diary_entries.append((timestamp, entry))
    print("Entry added successfully!")

# Function to view diary entries
def view_entries():
    if not diary_entries:
        print("No entries yet.")
        return

    current_entry = len(diary_entries) - 1
    while current_entry >= 0:
        timestamp, entry = diary_entries[current_entry]
        print("\nTimestamp:", timestamp)
        print("Entry:", entry)
        print("-" * 20)

        choice = input("Press 'N' for next entry, 'Q' to quit: ").upper()
        if choice == 'Q':
            break
        current_entry -= 1

# Main menu loop
while True:
    user_password = input("Enter password: ")
    
    if user_password != password:
        print("Incorrect password. Exiting...")
        break
    
    print("\nWelcome to your diary!")
    print("Options:")
    print("1. Add diary entry")
    print("2. View diary entries")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_entry()
    elif choice == '2':
        view_entries()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")

'''