# DESCRIPTION: A Magic the gathering tournment results tracker
# AUTHOR: Brian Janes   
# DATE: March 19th, 2024

# Import the necessary libraries
import math
import sys
import datetime
import FormatValues as FV
import os
import time

# Define the main function
print()
print("  M:TG Tournament Statistics Tracker")
print()
print()
while True:
    number_of_rounds = int(input("Enter the number of rounds: "))
    if number_of_rounds < 3:
        print("Please enter a number greater than 3")
    else:
        break
print()
tournament_format = input("Enter the format of the tournament:  ").title()

print()
user_deck_archetype = input("Enter the deck you played in the event: ").title()
# Create a list to store the results of each round
round_details = []

# Iterating over the 
for round in range(number_of_rounds):
    os.system('clear')
    print()
    print(f"Entering details for round {round + 1}:")
    print()
    # Get details for this round
    while True:
        play_draw = input("Did you play or draw this round? (P/D): ")
        if play_draw.upper() not in ["P", "D"]:
            print("Please enter P or D.")
        else:
            break
    matchup = input("What was the matchup this round?: ")

    # Get details for this round
    while True:
        result = input("Did you win, lose, or draw this match? (W/L/D): ")
        if result.upper() not in ["W", "L", "D"]:
            print("Please enter W, L, or D.")
        else:
            break

    # Initializing these variables to 0
    wins = 0
    losses = 0
    draws = 0

    if result.upper() == "W":
        wins = 2
        losses = int(input("How many games did you lose this round? (0 or 1): "))
    elif result.upper() == "L":
        losses = 2
        wins = int(input("How many games did you win this round? (0 or 1): "))
    elif result.upper() == "D":  
        wins = int(input("How many games did you win this round? (0 or 1): "))
        if wins == 1:
            losses = 1
            draws = 1
        else:
            losses = int(input("How many games did you lose this round? (0 or 1): "))
            draws = 1 if losses == 0 else 0

    # Initialize mulligan counters
    player_mulligans = 0
    opponent_mulligans = 0

    # Calculate total games
    total_games = wins + losses + draws

    # Ask for mulligan information for each game
    for game in range(total_games):
        print()
        player_mulligans += int(input(f"How many times did you mulligan in game {game + 1}?: "))
        opponent_mulligans += int(input(f"How many times did your opponent mulligan in game {game + 1}?: "))

    print()
    notes = input("Any notes for this round?: ")

print()
for _ in range(5):  # Change to control number of 'blinks'
    print('Preparing for next round...', end='\r')
    time.sleep(.3)  # To create the blinking effect
    sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
    time.sleep(.3)

# Clear the console at the end of each round
os.system('clear')

# Store details in a dictionary
round_detail = {
    "play_draw": play_draw,
    "player mulligans": player_mulligans,
    "opponent mulligans": opponent_mulligans,
    "matchup": matchup,
    "wins": wins,
    "losses": losses,
    "draws": draws,
    "notes": notes
}
# Add the details for this round to the list
round_details.append(round_detail)

print(round_detail)