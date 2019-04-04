#%% Imports
import itertools
import random
import numpy as np
from PIL import Image
import Deck_of_cards_w_brackets

#%% Variables
# 'C' are clubs, 'D' are diamonds, 'H' are hearts, 'S' are spades
Suit_list = ['C', 'D', 'H', 'S']
Value_list = ['2', '3', '4', '5', '6', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

#%% Creates the card class
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.Card = self,value, self.suit
    def __repr__(self):
        return self.value + self.suit

#Example to call card
print(Card('8', "D"))
#%% Creates deck class
class deck(set):
    def __init__(self):
        for value, suit in itertools.product(Value_list, Suit_list):
            self.add(Card(value, suit))
print(deck())
#%% Draw a random hand
def draw_a_hand():
    random_hand = random.sample(deck(), 5)
    return random_hand

draw_a_hand()
