def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def generate_number_list(start, end, step):
    number_list = list(range(start, end, step))
    return number_list


def main():
    print("Welcome to my number list generator.")
    print()
    print("You are going to give me a number you want to start with, an ending number, and by how many you want me to add each time.")
    print()

    start = get_int_input("What number do you want to start with? ")
    end = get_int_input("What number do you want to end with? ")
    step = get_int_input("How many should I add each time? ")

    number_list = generate_number_list(start, end, step)

    print("Generated Number List:")
    for number in number_list:
        print(number)


if __name__ == "__main__":
    main()
