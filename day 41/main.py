'''# Example 1: Creating a dictionary
person = {
    "name": "John Doe",
    "age": 30,
    "occupation": "Engineer",
    "email": "johndoe@example.com"

}
for name,value in person.items():
  print(f"{name}:{value}")
'''
'''
website = {"name": None, "url": None, "desc": None, "rating": None}

for name in website.keys():
  website[name] = input(f"{name}: ")

print()
for name, value in website.items():
  print(f"{name}: {value}")

'''


website = {"name": None, "url": None, "desc": None, "rating": None}

# Use a dictionary to store the prompt messages for each field
input_messages = {
    "name": "Enter the website name: ",
    "url": "Enter the website URL: ",
    "desc": "Enter a description for the website: ",
    "rating": "Enter the website rating: "
}

# Loop through the dictionary keys to get user input
for name, value in website.items():
    while True:
        user_input = input(input_messages[name])

        if name == "rating":
            try:
                website[name] = float(user_input)
            except ValueError:
                print("Invalid input. Please enter a number for the rating.")
            else:
                break
        elif user_input.strip():
            website[name] = user_input
            break
        else:
            print("This field cannot be left empty. Please try again.")

print("\nWebsite Details:")
for name, value in website.items():
    print(f"{name.capitalize()}: {value}")


'''
# Example 2: Creating an empty dictionary and adding values later
student = {}
student["name"] = "Alice"
student["age"] = 22
student["major"] = "Computer Science"

# Example 3: Using dict() constructor to create a dictionary
employee = dict(
    name="Jane Smith",
    age=25,
    department="Human Resources",
    email="janesmith@example.com"
)

# Printing the dictionaries
print(person)
print(student)
print(employee)

'''