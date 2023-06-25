print("Welcome to Guess the Number.")
print()
print("Guess a number between 1 and 1,000,000, and I will tell you if you are too low, too high, or correct.")
print()
print("Let's play!")

correct_number = 2300
attempt = 0

while True:
    attempt += 1
    user_guess = input("Pick a number between 1 and 1,000,000 (or enter 'q' to quit): ")
    
    if user_guess.lower() == 'q':
        print("Now we'll never know what the answer is...")
        exit()
    
    try:
        user_guess = int(user_guess)
    except ValueError:
        print("That is not a valid number. Try again!")
        continue
    
    if user_guess < correct_number:
        print("That number is too low. Try again!")
    elif user_guess > correct_number:
        print("That number is too high. Try again!")
    else:
        print("You are a winner! 🥳🥳")
        break

print("It took you", attempt, "attempt(s) to find the correct answer.")