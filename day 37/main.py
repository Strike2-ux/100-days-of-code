
'''print("STAR WARS NAME GENERATOR")

all = input("Enter your first name, last name, Mum's maiden name and the city you were born in").split()

first = all[0].strip()
last = all[1].strip()
maiden = all[2].strip()
city = all[3].strip()

name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"

print(f"Your Star Wars name is {name}")'''

def generate_star_wars_name():
    print("STAR WARS NAME GENERATOR")

    input_str = input("Enter your first name, last name, Mum's maiden name, and the city you were born in (separated by spaces): ")

    data = input_str.split()

    if len(data) < 4:
        print("Please enter all four pieces of information.")
        return

    first_name = data[0].strip()
    last_name = data[1].strip()
    maiden_name = data[2].strip()
    city_name = data[3].strip()

    if len(first_name) < 3 or len(last_name) < 3 or len(maiden_name) < 2 or len(city_name) < 3:
        print("Please enter valid names with at least 3 characters for first name and last name, and 2 characters for maiden name and city name.")
        return

    star_wars_name = f"{first_name[:3].title()}{last_name[:3].lower()} {maiden_name[:2].title()}{city_name[-3:].lower()}"

    print(f"Your Star Wars name is {star_wars_name}")

generate_star_wars_name()
