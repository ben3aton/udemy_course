"""Module to handle the extended lottery challenge"""

import random
import numpy as np

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

top_player = players[0]

matching_numbers = [len(x['numbers'].intersection(lottery_numbers)) for x in players]
winning_player = players[np.argmax(matching_numbers)]
print(f"Winning Player = {winning_player['name']} with a total of {np.argmax(matching_numbers)} winning numbers")
