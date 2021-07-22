"""Module to handle the extended lottery challenge"""

import random

lottery_numbers = set(random.sample(range(22), 6))  # Generate a random set of 6 numbers from 1 to 22

players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 22, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}} # Do a dictionary of 4 players that have their name and numbers either side of the dictionary
]

top_player = players[0] # Start by naming the first player in the game the top player to allow for comparison later on

for player in players: # Create a for loop that iterates over each of the players in the players list, calling the new variable player
    matched_numbers = len(player["numbers"].intersection(lottery_numbers)) # calculate how many matching numbers each player got
    if matched_numbers > len(top_player["numbers"].intersection(lottery_numbers)): # compare the most matched player with the already asssigned top player
            top_player = player # if statement is true then reassign the top player

winnings = 100 ** len(top_player["numbers"].intersection(lottery_numbers)) # create a formulated amount for the winnings

print(f"{top_player['name']} won {winnings}.") # finish off with the statement of who won and how much they won