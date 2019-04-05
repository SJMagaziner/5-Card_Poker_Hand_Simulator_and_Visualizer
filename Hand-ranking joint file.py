#%%

th = list(random.sample(deck2, 5))
print(th)

#Dictionary calls for ranks (cdv) and suits (cds)
cdv1 = rank_dictionary[(str((th[0]))[2:3])]
cdv2 = rank_dictionary[(str((th[1]))[2:3])]
cdv3 = rank_dictionary[(str((th[2]))[2:3])]
cdv4 = rank_dictionary[(str((th[3]))[2:3])]
cdv5 = rank_dictionary[str((th[4]))[2:3]]

cds1 = suit_dictionary[(str((th[0]))[3:4])]
cds2 = suit_dictionary[(str((th[1]))[3:4])]
cds3 = suit_dictionary[(str((th[2]))[3:4])]
cds4 = suit_dictionary[(str((th[3]))[3:4])]
cds5 = suit_dictionary[str((th[4]))[3:4]]

hs = [cds1, cds2, cds3, cds4, cds5]
hs.sort(reverse=True)
hv = [cdv1, cdv2, cdv3, cdv4, cdv5]
hv.sort(reverse=True)

def hand_class():
    hand_rank = "High Card!"
    if len(set(hs)) == 1 and (hv[0] == hv[4]+4 or hv==[13, 4, 3, 2, 1]):
        hand_rank = 'Straight Flush'
    elif len(set(hv)) == 2 and (hv[0] == hv[3] or hv[1]== hv[4]):
        hand_rank = 'Four of a Kind'
    elif len(set(hv)) == 2:
        hand_rank = 'Full House!'
    elif len(set(hs)) == 1:
        hand_rank = 'Flush!'
    elif hv[0]==hv[4]+4 or hv == [13, 4, 3, 2, 1]:
        hand_rank = 'Straight!'
    elif len(set(hv)) == 3 and (hv[0] == hv[2] or hv[2] == hv[4]):
        hand_rank = 'Three of a Kind!'
    elif len(set(hv)) == 3:
        hand_rank = 'Two Pair!'
    elif len(set(hv)) == 4:
        hand_rank = 'Pair!'

    print(hand_rank)

hand_class()
