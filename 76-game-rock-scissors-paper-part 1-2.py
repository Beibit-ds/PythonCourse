import random

options = {
    0: "rock",
    1: "scissors",
    2: "paper"
}
player_1 = random.randint(0,2)
player_2 = random.randint(0,2)
print(f"Player 1 selected: {player_1, options[player_1]}")
print(f"Player 2 selected: {player_2, options[player_2]}")
if player_1 == 0 and player_2 == 1:
    print('Player 1 wins')
elif player_1 == 0 and player_2 == 2:
    print('Player 2 wins')
elif player_1 == 1 and player_2 == 0:
    print('Player 2 wins')
elif player_1 == 1 and player_2 == 2:
    print('Player 1 wins')
elif player_1 == 2 and player_2 == 0:
    print('Player 1 wins')
elif player_1 == 2 and player_2 == 1:
    print('Player 2 wins')
else:
    print('Draw!')