# intro
import time
import random

print("Starting", end="", flush=True)

# Countdown timer: 3... 2... 1...
for i in range():
    time.sleep(1)
    print(f" {i}", end="", flush=True)


print("")


print("Welcome to my Rock,Paper,Scissors!", end="", flush=True)
time.sleep(1)
print(" ")
print( flush=True)


print(" ")
game = ["Rock", "Paper", "Scissors"]

# Ask for player 1 input (convert to lowercase right away)
player1 = input("Player 1, choose Rock, Paper, or Scissors: ").lower()

# Validate input — keep asking until valid
while player1 not in game:
    player1 = input(
        "That's not a valid choice! Please type 'rock', 'paper', or 'scissors': "
    ).lower()

# Computer randomly chooses
player2 = random.choice(game)


rock = "Rock"
paper = "Paper"
scissors = "Scissors"

print("", end="", flush=True)

# Countdown / animation with delays
time.sleep(1)
print("Rock", flush=True)
time.sleep(1)
print("Paper", flush=True)
time.sleep(1)
print("Scissors", flush=True)
time.sleep(1)
print("Shoot!", flush=True)

# Results
print("\n")
print(f"Player 1 chose: {player1}")
print(f"Player 2 chose: {player2}")

print("")
time.sleep(1)

# Determine winner
if player1 == player2:
    print("It's a tie!")
elif (
    (player1 == "rock" and player2 == "scissors")
    or (player1 == "paper" and player2 == "rock")
    or (player1 == "scissors" and player2 == "paper")
):
    print("Player 1 wins! 🎉")
else:
    print("Computer wins! 🤖")