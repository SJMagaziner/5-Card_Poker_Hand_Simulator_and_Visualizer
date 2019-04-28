#%% Global variables and definitions

# 'C' are clubs, 'D' are diamonds, 'H' are hearts, 'S' are spades
Suit_list = ['C', 'D', 'H', 'S']
# Numeric corresponds to rank with 'T' for 10, 'J' for Jack, 'Q' for Queen, 'K' for King, and 'A' for Ace
Value_list = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

# Making a deck using lists instead of new class functions
deck2 = [[v + s] for s in Suit_list for v in Value_list]

# These dictionaries are used to pull from the card call the values of each assigned and suit for use in hand determination
rank_dictionary = {
        '2': 1,
        '3': 2,
        '4': 3,
        '5': 4,
        '6': 5,
        '7': 6,
        '8': 7,
        '9': 8,
        'T': 9,
        'J': 10,
        'Q': 11,
        'K': 12,
        'A': 13
        }
suit_dictionary = {
        'S': 4,
        'H': 3,
        'D': 2,
        'C': 1
        }