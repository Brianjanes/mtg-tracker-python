# DESCRIPTION: A Magic the gathering tournment results tracker
# AUTHOR: Brian Janes   
# DATE: March 19th, 2024

# Import the necessary libraries
import sys
import os
import time
import uuid
import mtg_functions as my_funcs

# Define the main function
print()
print("   M:TG Tournament Statistics Tracker")
print("  ------------------------------------------------------------")
print()

while True:
    tournament_name = "brian's tournamemt" # input("Enter the name of the tournament: ")
    print()
    number_of_rounds = 3 #int(input("Enter the number of rounds: "))
    if number_of_rounds < 3:
        print("Please enter a number greater than 3")
    else:
        break
print()
tournament_format = "standard" # input("Enter the format of the tournament:  ").title()

print()
user_deck_archetype = "UB Midrange" # input("Enter the deck you played in the event: ").title()

# Create a list to store the results of each round
round_details = {}

# Iterating over the 
for round in range(number_of_rounds):
    os.system('clear')
    print()
    print(f"Entering details for round {round + 1}:")
    print()
    # Get details for this round
    while True:
        # Play/Draw input
        play_draw = input("Did you play or draw this round? (P/D): ")
        if play_draw.upper() not in ["P", "D"]:
            print("Please enter P or D.")
        else:
            break

    # Matchup input - would be good to add some logic to mirror match
    matchup = input("What did you play against this round?: ")

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
        round_outcome = "win"
        wins = 2
        losses = int(input("How many games did you lose this round? (0 or 1): "))
    elif result.upper() == "L":
        round_outcome = "loss"
        losses = 2
        wins = int(input("How many games did you win this round? (0 or 1): "))
    elif result.upper() == "D": 
        round_outcome = "draw"
        wins = int(input("How many games did you win this round? (0 or 1): "))
        if wins == 1:
            losses = 1
            draws = 1

    # Initialize mulligan counters
    player_mulligans = 0
    opponent_mulligans = 0

    # Calculate total games
    total_games = wins + losses + draws

    # Generate a unique ID for each tournament
    tournament_id = uuid.uuid4()

    # Ask for mulligan information for each game
    print()
    print(f"You played a total of {total_games} games this round.")
    print(f"This led to an opportunity for {total_games} mulligans.")
    for game in range(total_games):
        print()
        while True:
            try:
                # Checking to make sure that the value entered is a number.
                player_mulligans += int(input(f"How many times did you mulligan in game {game + 1}?: "))
                if player_mulligans < 0:
                    print("Please enter a number greater than 0.")
                else:
                    break
            except ValueError:
                print("Please enter a positive number.")
            
        while True:
            try:
                # Checking to make sure that the value entered is a number.
                opponent_mulligans += int(input(f"How many times did your opponent mulligan in game {game + 1}?: "))
                if opponent_mulligans < 0:
                    print("Please enter a number greater than 0.")
                else:
                    break
            except ValueError:
                print("Please enter a positive number.")

    print()
    notes = "no notes at this time" # input("Any notes for this round?: ")

    opp_w_on_mull_rate = my_funcs.opp_mull_win_rate(opponent_mulligans, wins, losses)
    my_w_on_mull_rate = my_funcs.player_mull_win_rate(player_mulligans, wins, losses)

    # Store the mulligan details in a dictionary
    mull_dict = {
        "opponent mulligans": opponent_mulligans,
        "player mulligans": player_mulligans,
        "opponent's win rate on mulligans": opp_w_on_mull_rate,
        "player's win rate on mulligans": my_w_on_mull_rate
    }

    # Store the matchup details in a dictionary
    matchup_dict = {
        "matchup": matchup,
        "round outcome": round_outcome,
        "wins": wins,
        "losses": losses,
        "draws": draws
    }

    # Store details in a dictionary
    round_detail = {
        "play/draw": play_draw,
        "mulligan info:" : mull_dict,
        "matchup": matchup_dict,
        "round outcome": round_outcome,
        "match notes": notes
        }
    
    # Add the details for this round to the dictionary
    round_details["Round #", round + 1] = round_detail

    # After all rounds are collected, store them under the tournament ID
    tournaments = [{tournament_id: round_details}]

    # Calculate matchup spread - I want to iterate over the matchup spread array and check for duplicates and then determine how many different matcups I played against.
    # Create a list for matchups later. I want to know how many different decks I played against in a tournament.
    matchup_spread = []
    matchup_spread.append(matchup)

    # Initialize a dictionary to store the matchup counts
    matchup_counts = {}

# Iterate over the matchups array
for matchup in matchup_spread:
    # If the matchup is already in the dictionary, increment its count
    if matchup in matchup_counts:
        matchup_counts[matchup] += 1
    # Otherwise, add the matchup to the dictionary with a count of 1
    else:
        matchup_counts[matchup] = 1

    # After all rounds are collected, print a summary of the tournament
    print()
    print("Tournament Summary:")
    print()
    for round_number, round_detail in round_details.items():
        print(f"Round {round_number}:")
        print(f"  Matchup: {round_detail['matchup']}")
        print(f"  Round Outcome: {round_detail['round outcome']} in {total_games}")
        # Print the matchup counts
        for matchup, count in matchup_counts.items():
            print(f"{matchup}: {count}")
        print()
        print(f"  Notes: {round_detail['match notes']}")
        print()
        print(f"  Total Player Mulligans: {round_detail['player mulligans']}")
        print(f"  Total Opponent Mulligans: {round_detail['opponent mulligans']}")
        print()
        print(f"  Player's Win Rate on Mulligans: {round_detail['player\'s win rate on mulligans']}")
        print(f"  Opponent's Win Rate on Mulligans: {round_detail['opponent\'s win rate on mulligans']}")
        print()
        print()

print()
for _ in range(5):  # Change to control number of 'blinks'
    print('Preparing for next round...', end='\r')
    time.sleep(.3)  # To create the blinking effect
    sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
    time.sleep(.3)

# Clear the console at the end of each round
os.system('clear')

print(tournaments)

# Stepping away for the night on 19/03/2024 - receipt is not printing properly, i am not sure why, it seems like it can't access some data because it's nested differently now because I added the dictionaries for organization. Will sort out tomorrow or the next time i come to this project.

# Next things to do are refactor inputs to ask who won game 1 and who started OTP, and work out the logic for the rest of that so that OTP win % and OTD win % can be tracked!