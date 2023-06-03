from getpass import getpass as input

import getpass


def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif player1_choice == 'R':
        if player2_choice == 'S':
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    elif player1_choice == 'P':
        if player2_choice == 'R':
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    elif player1_choice == 'S':
        if player2_choice == 'P':
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"

def play_game():
    print("EPIC  \U0000270A,  \U0000270B,  \U0000270C  BATTLE!")
    print("Player 1, enter your choice: ")
    player1_choice = getpass.getpass("Player 1 choice: ").upper()

    valid_choices = ['R', 'P', 'S']
    while player1_choice not in valid_choices:
        print("Invalid choice. Please try again.")
        player1_choice = getpass.getpass("Player 1 choice: ").upper()

    print("\n" * 100)  # Clear the console screen

    print("Player 2, enter your choice: ")
    player2_choice = getpass.getpass("Player 2 choice: ").upper()
    while player2_choice not in valid_choices:
        print("Invalid choice. Please try again.")
        player2_choice = getpass.getpass("Player 2 choice: ").upper()

    print("\n" * 100)  # Clear the console screen

    print(f"Player 1 choice: {player1_choice}")
    print(f"Player 2 choice: {player2_choice}")

    result = determine_winner(player1_choice, player2_choice)
    print(result)

input = getpass.getpass  # Use getpass.getpass as input
play_game()

