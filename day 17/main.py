from getpass import getpass

print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()

player1_score = 0
player2_score = 0

while True:
    player1Move = getpass("Player 1 > ").upper()
    print()
    player2Move = getpass("Player 2 > ").upper()
    print()

    if player1Move == player2Move:
        print("You both picked", player1Move + ", draw!")
    elif (
        (player1Move == "R" and player2Move == "S")
        or (player1Move == "P" and player2Move == "R")
        or (player1Move == "S" and player2Move == "P")
    ):
        print("Player1 wins!")
        player1_score += 1
    else:
        print("Player2 wins!")
        player2_score += 1

    print("Player 1 has", player1_score, "wins.")
    print("Player 2 has", player2_score, "wins.")

    if player1_score == 3 or player2_score == 3:
        print("Thanks for playing!")
        break
    else:
        continue
