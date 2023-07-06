import random
from termcolor import colored

def roll_dice(sides):
    return random.randint(1, sides)

def generate_health_stats():
    six_sided = roll_dice(6)
    eight_sided = roll_dice(8)
    health_stats = six_sided * eight_sided
    return health_stats

def print_health_stats(name, health_stats):
    color = random.choice(['red', 'green', 'yellow', 'blue', 'magenta', 'cyan'])
    health_stats_text = colored(str(health_stats), color)
    print(f"{name}'s Health Stats: {health_stats_text}")

def generate_character_stats():
    print("⚔️ CHARACTERS STATS GENERATOR ⚔️")
    name = input("Enter the character's name: ")
    health_stats = generate_health_stats()
    print_health_stats(name, health_stats)

def play_game():
    while True:
        generate_character_stats()
        
        choice = input("Generate health stats for another character? (yes/no): ")
        if choice.lower() != "yes":
            print("Thank you for playing!")
            break

play_game()