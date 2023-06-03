# Get user input
test_name = False
user_score = False
max_score = False
taza = user_score >= 0 or user_score <= 100  
print("Choose wisely from the list of the subjects:\ncomputer science\nmathematics\nchemistry\nphysics\nlanguage")
test_name = input("Enter the name of the test: ")
test_name = test_name.lower()
user_score = int(input("Enter the user's score: "))
# conditions for the user score
if user_score == taza:
    pass
else:
    print("please put a real number")

# conditions for test_name
if test_name == "computer science":
    max_score = 100
elif test_name == "mathematics":
    max_score = 100
elif test_name == "chemistry":
    max_score = 80
elif test_name == "physics":
    max_score = 80
elif test_name == "language":
    max_score = 100
else:
    print("invalid class, you should choose from the ones of the list")

# Calculate percentage
percentage = round((user_score / max_score) * 100, 2)
# Determine letter grade
if percentage >= 90:
    letter_grade = "A+"
elif percentage >= 80:
    letter_grade = "A"
elif percentage >= 70:
    letter_grade = "B"
elif percentage >= 60:
    letter_grade = "C"
elif percentage >= 50:
    letter_grade = "D"
elif percentage  >= 0 or percentage <= 49:
    letter_grade = "U"
else:
    print("please use valid characters")
    exit()

# Display results
print("\nTest: " + test_name)
print("Percentage: " + str(percentage) + "%")
print("Letter Grade: " + letter_grade)
# Add emojis based on the letter grade
if letter_grade == "A+" or letter_grade == "A":
    print("🎉 Congratulations! Great job!")
elif letter_grade == "B":
    print("👍 Well done!")
elif letter_grade == "C":
    print("🙂 You did okay.")
elif letter_grade == "D":
    print("😕 You could have done better.")
else:
    print("😔 You need to improve.")


