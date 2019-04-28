#%% MAIN PROGRAM: Auto hand-drawer, visualizer, and data compiler

# Enter the number of hands you desire to generate
how_many_hands = 100

# Do you want images to appear for each hand (if yes, input 1, if false input 0?
#### TOO MANY HAND IMAGES BEING GENERATED WILL SLOW DOWN YOUR COMPUTER GREATLY
make_images_appear = False

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
