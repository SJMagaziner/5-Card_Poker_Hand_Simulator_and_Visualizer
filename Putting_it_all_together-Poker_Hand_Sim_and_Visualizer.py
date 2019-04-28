#%% Imports
#
#
#
import random
from PIL import Image
import datetime
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt


# Global variables and definitions
#
#
#
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

# Functions used in main program
#
#
#
def draw_a_hand():
    '''This function draws a random sample of 5 cards from the defined deck; each sample is unique
    and selected at random'''
    random_hand = random.sample(deck2, 5)
    return random_hand

def check_hand_values_and_suits():
    ''''Looks hand rank and suit values in dictionaries. Arranges the called values into a list of ints;
    .sort with reverse=True sorts in descending numerical order
        # E.g. a hand of [K,5,A,T,J] is sorted into [A,K,J,T,5]; same applies for suits
        # For brevity, hs and hv stand for "Hand suits" and "Hand values", respectively'''
    # Looks up rank values in dictionary (e.g. cdv1 is card 1's rank; A corresponds to 13, King to 12, etc.)
    cdv1 = rank_dictionary[(str((sorted_hand[0]))[2:3])]
    cdv2 = rank_dictionary[(str((sorted_hand[1]))[2:3])]
    cdv3 = rank_dictionary[(str((sorted_hand[2]))[2:3])]
    cdv4 = rank_dictionary[(str((sorted_hand[3]))[2:3])]
    cdv5 = rank_dictionary[str((sorted_hand[4]))[2:3]]

    # Looks up suit values in dictionary (e.g. cds1 is card 1's suit; Spades corresponds to 4, etc.)
    cds1 = suit_dictionary[(str((sorted_hand[0]))[3:4])]
    cds2 = suit_dictionary[(str((sorted_hand[1]))[3:4])]
    cds3 = suit_dictionary[(str((sorted_hand[2]))[3:4])]
    cds4 = suit_dictionary[(str((sorted_hand[3]))[3:4])]
    cds5 = suit_dictionary[str((sorted_hand[4]))[3:4]]

    # Arranges the called values into a list of ints; .sort with reverse=True sorts in descending numerical order
    # E.g. a hand of [K,5,A,T,J] is sorted into [A,K,J,T,5]; same applies for suits
    # For brevity, hs and hv stand for "Hand suits" and "Hand values", respectively
    hs = [cds1, cds2, cds3, cds4, cds5]
    hs.sort(reverse=True)
    hv = [cdv1, cdv2, cdv3, cdv4, cdv5]
    hv.sort(reverse=True)
    return hs, hv

def what_is_the_hand_rank():
    '''Defines hand ranks; the len(set(hs)) and len(set(hv)) functions look for unique values in the hv or hs lists
    E.g. A flush (all same suit) possesses only one unique suit value, thus len(set(hs)) == 1
        Since ranks are numbered, other relations appear such as straights always possessing a range of 4
    Exceptions exist and are noted/coded as appropriate
        E.g. a hand of len(set(hv)) == 2 can be either [A,A,A,K,K] or [A,A,A,A,K]
            These hands can be further differentiated by whether the 1st and 4th or 2nd and 5th cards have == values
            If they do, they must be four of a kind, if not, they must be full houses
    The default rank is a high card; Elif statements alter this variable if the proper conditions are met'''
    hand_rank = "High Card"
    if len(set(hs)) == 1 and hv == [13, 12, 11, 10, 9]:
        hand_rank = 'Royal Flush'
    elif len(set(hs)) == 1 and (hv[0] == hv[4] + 4 or hv == [13, 4, 3, 2, 1]):
        hand_rank = 'Straight Flush'
    elif len(set(hv)) == 2 and (hv[0] == hv[3] or hv[1] == hv[4]):
        hand_rank = 'Four of a Kind'
    elif len(set(hv)) == 2:
        hand_rank = 'Full House'
    elif len(set(hs)) == 1:
        hand_rank = 'Flush'
    elif (hv[0] == hv[4] + 4 and len(set(hv)) == 5) or hv == [13, 4, 3, 2, 1]:
        hand_rank = 'Straight'
    elif len(set(hv)) == 3 and (hv[0] == hv[2] or hv[2] == hv[4]):
        hand_rank = 'Three of a Kind'
    elif len(set(hv)) == 3:
        hand_rank = 'Two Pair'
    elif len(set(hv)) == 4:
        hand_rank = 'Pair'
    return hand_rank

def make_poker_hand_images():
    '''This function calls the stored card image associated with each file.  It then extracts their data
    including dimensions and coloring (e.g. RGB, CYMK, etc), stitches them together, and displays the new
    image.  By changing the directories and image names, one can stitch any images together'''
    # This calls the png file associated with each card the player draws
    card1_file = str(sorted_hand[0]) + '.png'
    card2_file = str(sorted_hand[1]) + '.png'
    card3_file = str(sorted_hand[2]) + '.png'
    card4_file = str(sorted_hand[3]) + '.png'
    card5_file = str(sorted_hand[4]) + '.png'
    # This employs the package 'pillow' to read the images to later extract data
    card1 = Image.open('Deck_of_cards_with_parentheses/' + card1_file)
    card2 = Image.open('Deck_of_cards_with_parentheses/' + card2_file)
    card3 = Image.open('Deck_of_cards_with_parentheses/' + card3_file)
    card4 = Image.open('Deck_of_cards_with_parentheses/' + card4_file)
    card5 = Image.open('Deck_of_cards_with_parentheses/' + card5_file)

    # the X.size module extracts the pixel height and width of each image
    (width1, height1) = card1.size
    (width2, height2) = card2.size
    (width3, height3) = card3.size
    (width4, height4) = card4.size
    (width5, height5) = card5.size

    # This function defines the new composite image size (i.e. a combo of 5 cards)
    result_width = width1 + width2 + width3 + width4 + width5
    result_height = max(height1, height2, height3, height4, height5)

    # The final hand image is a new photo generated by stitching the card files at the appropriate locations within a-
    # 2D box (the new box is a result of the combination of widths)
    hand = Image.new('RGB', (result_width, result_height))
    hand.paste(im=card1, box=(0, 0))
    hand.paste(im=card2, box=(width1, 0))
    hand.paste(im=card3, box=(width1 + width2, 0))
    hand.paste(im=card4, box=(width1 + width2 + width3, 0))
    hand.paste(im=card5, box=(width1 + width2 + width3 + width4, 0))

    # Function to show the newly made image
    Image._show(hand)

#%% MAIN PROGRAM: Auto hand-drawer, visualizer, and data compiler

# Enter the number of hands you desire to generate
how_many_hands = 3

# Do you want images to appear for each hand (if yes, input 1, if false input 0?
#### TOO MANY HAND IMAGES BEING GENERATED WILL SLOW DOWN YOUR COMPUTER GREATLY
make_images_appear = True

# Generates empty pandas dataframe onto which we will append info from each hand
poker_hands_df = pd.DataFrame()

# Hand counter
hand_counter = 0

# Current time:
StartTime = datetime.datetime.now()

for i in range(how_many_hands):
    # Notifies which hand the player is currently on
    hand_counter = hand_counter + 1
    print('This is hand #' + str(hand_counter))

    # This draws one's unique 5-card hand and sorts it, grouping like cards
    random_hand = draw_a_hand()
    sorted_hand = sorted(random_hand)
    print(sorted_hand)

    # Pulls hand values and suits for use in rank checking, see function documentation for detailed explanation
    hs = check_hand_values_and_suits()[0]
    hv = check_hand_values_and_suits()[1]

    # Defines hand ranks; see function documentation for detailed explanation
    hand_rank = what_is_the_hand_rank()
    print(hand_rank)

    # Creates a time stamp for each hand iteration
    current_time = datetime.datetime.now()
    time_diff = current_time - StartTime
    print(time_diff)

    # This generates a pandas dataframe for the most recent hand drawn
    add_hand = pd.DataFrame({'Hand Rank': hand_rank,
                             'Card 1': sorted_hand[0],
                             'Card 2': sorted_hand[1],
                             'Card 3': sorted_hand[2],
                             'Card 4': sorted_hand[3],
                             'Card 5': sorted_hand[4],
                             'Time to completion': str(time_diff)})

    # This will append the most recently drawn hand to the empty/existing pandas dataframe
    poker_hands_df = poker_hands_df.append(add_hand)

    # This argument will return an image for each hand drawn (if noted by player)
    # It can be used to stitch any images together, just change pathways and names of the function
    # See function documentation for more information
    if make_images_appear == 1:
        make_poker_hand_images()

# Lastly, this will store the dataframe as an excel sheet entitled 'Poker Statistics'
# While the variable poker_hands_df will be the appropriate, complete dataframe, this ensures the data is saved
if how_many_hands == hand_counter:
    with pd.ExcelWriter('Data/Poker Hand Statistics.xlsx') as writer:
        poker_hands_df.to_excel(writer, sheet_name='Sheet1')
    print(poker_hands_df)

#%% Working with the data
#
#
#

# Builds two dataframes (rank count [rc] and card occurrence [co] from an existing data set)
expected_rc_df = pd.read_excel('Data/Expected poker hand outcomes.xlsx', sheet_name='Ranks')
expected_co_df = pd.read_excel('Data/Expected poker hand outcomes.xlsx', sheet_name='Cards')

# Builds a dataframe from an existing sample of 1 million poker hands simulated using this code
# NOTE: THIS CAN TAKE A FEW MINUTES AS IT IS PROCESSING A MASSIVE DATA SET
million_hand_df = pd.read_excel('Data/Poker Hand Statistics 1mil.xlsx')

#%% Assessing Hand Rank (all ranks)
#
#
#

# Counts resultant hand ranks counts (rc)
Rank_counts = Counter(million_hand_df['Hand Rank'])

# 1) Generates a new dataframe based on previous count, 2) Renames the column default column name of 0 to 'Simulated',
# 3) and re-orders the index in ascending hand rank for use in later plotting applications
rc_all_df = pd.DataFrame.from_dict(Rank_counts, orient='index').rename(index=str, columns={0: 'Simulated'}).reindex(['High Card', 'Pair', 'Two Pair', 'Three of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind','Straight Flush', 'Royal Flush'])

# Calls upon an excel sheet containing the expected hand rank outcomes according to statistics and adds it to rc_df
rc_all_df['Expected'] = expected_rc_df.loc[:,'Expected']

# Generates a bar plot comparing simulated vs. expected hand rank outcomes (all)
rc_graph1 = rc_all_df.plot(kind='bar')
plt.Axes.tick_params(self=rc_graph1, axis='x', labelsize=10, labelrotation=45)
plt.ylabel('Number of times drawn', fontsize=12)
plt.xlabel('Rank', fontsize=12)
plt.title('Rank Occurrence in 1 Million 5-card Poker Hands', fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.savefig('Figures/Hand_Rank_Outcomes_(High_Card_to_Royal_Flush).png', dpi='figure')
plt.show()

# Zoomed in look at hand ranks (Straight to Royal)
#
#
#

# 1) Generates a new dataframe based on previous count, 2) Renames the column default column name of 0 to 'Simulated',
# 3) and re-orders the index in ascending hand rank for use in later plotting applications
rc_straight_to_royal_df = pd.DataFrame.from_dict(Rank_counts, orient='index').rename(index=str, columns={0: 'Simulated'}).reindex(['Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush', 'Royal Flush'])

# Calls upon an excel sheet containing the expected hand rank outcomes according to statistics and adds it to rc_df
rc_straight_to_royal_df['Expected'] = expected_rc_df.loc['Straight':'Royal Flush','Expected']

# Generates a bar plot comparing simulated vs. expected hand rank outcomes (Straight to Royal)
rc_graph2 = rc_straight_to_royal_df.plot(kind='bar')
plt.Axes.tick_params(self=rc_graph2, axis='x', labelsize=10, labelrotation=45)
plt.ylabel('Number of times drawn', fontsize=12)
plt.xlabel('Rank', fontsize=12)
plt.title('Rank Occurrence in 1 Million 5-card Poker Hands', fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.savefig('Figures/Hand_Rank_Outcomes_(Straight_to_Royal_Flush).png', dpi='figure')
plt.show()

# Zoomed in look at hand ranks (Straight Flush to Royal)
#
#
#

# 1) Generates a new dataframe based on previous count, 2) Renames the column default column name of 0 to 'Simulated',
# 3) and re-orders the index in ascending hand rank for use in later plotting applications
rc_sflush_to_royal_df = pd.DataFrame.from_dict(Rank_counts, orient='index').rename(index=str, columns={0: 'Simulated'}).reindex(['Straight Flush', 'Royal Flush'])

# Calls upon an excel sheet containing the expected hand rank outcomes according to statistics and adds it to rc_df
rc_sflush_to_royal_df['Expected'] = expected_rc_df.loc['Straight Flush':'Royal Flush','Expected']

# Generates a bar plot comparing simulated vs. expected hand rank outcomes (Straight Flush to Royal)
rc_graph3 = rc_sflush_to_royal_df.plot(kind='bar')
plt.Axes.tick_params(self=rc_graph3, axis='x', labelsize=10, labelrotation=45)
plt.ylabel('Number of times drawn', fontsize=12)
plt.xlabel('Rank', fontsize=12)
plt.title('Rank Occurrence in 1 Million 5-card Poker Hands', fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.savefig('Figures/Hand_Rank_Outcomes_(Straight_Flush_to_Royal_Flush).png', dpi='figure')
plt.show()

# Working with the data (card occurrence)
#
#
#

# Counts resultant card occurrences (co)
c1o = Counter(million_hand_df['Card 1'])
c2o = Counter(million_hand_df['Card 2'])
c3o = Counter(million_hand_df['Card 3'])
c4o = Counter(million_hand_df['Card 4'])
c5o = Counter(million_hand_df['Card 5'])
Card_counts = c1o+c2o+c3o+c4o+c5o

# 1) Generates a new dataframe based on previous count, 2) Renames the column default column name of 0 to 'Simulated',
# 3) and re-orders the index in ascending card value for use in later plotting applications
co_total_df = pd.DataFrame.from_dict(Card_counts, orient='index').rename(index=str, columns={0: 'Simulated'}).sort_index()

# Calls upon an excel sheet containing the expected hand rank outcomes according to statistics and adds it to cc_total_df
co_total_df['Expected'] = expected_co_df.loc[:,'Expected']

# Generates bargraph
co_graph = co_total_df.plot(kind='bar')
plt.Axes.tick_params(self=co_graph, axis='x', labelsize=8, labelrotation=90)
plt.ylabel('Number of times drawn', fontsize=12)
plt.xlabel('Card', fontsize=12)
plt.title('Card Occurrence in a 52-card deck', fontsize=14)
plt.tight_layout()
plt.savefig('Figures/Card_Occurrence.png', dpi='figure')
plt.show()

# Hands Drawn vs Time to completion (1 mil)
#
#
#

mil_time_course = {'Hand #': [1, 10, 100, 1000, 10000, 50000, 100000, 250000, 500000, 750000, 1000000],
                'Time (hrs)': [0, .0000083 , .0001222, .001219, .013675, .131519, .4569344, 2.46253, 9.35619, 20.3511, 35.2033]}

mil_time_course_df = pd.DataFrame(data=mil_time_course)

plt.plot(mil_time_course_df['Time (hrs)'], mil_time_course_df['Hand #'])
plt.ylabel('Hand #', fontsize=12)
plt.xlabel('Time (hrs)', fontsize=12)
plt.title('Poker Hand Simulator: Runtime vs. Hand #', fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.savefig('Figures/Hands_drawn_over_time.png', dpi='figure')
plt.show()

#%% Hands drawn time comparison of with image and without
#
#
#

hand_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
with_image = [0.00000, 3.859634, 6.07011, 8.167023, 10.159657, 12.161241, 14.158741, 16.168040, 18.141908, 20.148223]
without_image = [0.00000, 0.00725, 0.015625, 0.015625, 0.015625, 0.031243, 0.031243, 0.031243, 0.046864, 0.046864]

plt.plot(with_image, hand_num, color='blue', label='With Image')
plt.plot(without_image, hand_num, color='orange', label='Without Image')

plt.legend()
plt.ylabel('Hand #', fontsize=12)
plt.xlabel('Time (sec)', fontsize=12)
plt.title('Poker Hand Simulator: Effects of Generating Images on Runtime', fontsize=14)
plt.tight_layout()
plt.savefig('Figures/Effects_of_generating_image1.tif', dpi='figure')
plt.show()
