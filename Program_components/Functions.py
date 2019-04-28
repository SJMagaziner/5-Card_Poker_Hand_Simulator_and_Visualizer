#%% Functions used in main program

def draw_a_hand():
    '''This function draws a random sample of 5 cards from the defined deck; each sample is unique
    and selected at random.'''
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