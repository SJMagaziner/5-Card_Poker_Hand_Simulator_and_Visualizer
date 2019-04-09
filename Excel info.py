import xlwt as xcell
import pandas as pd

#%%
random_hand = [['2D'], ['3C'], ['3D'], ['TD'], ['TS']]
hand_rank = 'Pair!'
hand_df = pd.DataFrame({'Hand Rank': hand_rank,
                        'Card 1': random_hand[0],
                        'Card 2': random_hand[1],
                        'Card 3': random_hand[2],
                        'Card 4': random_hand[3],
                        'Card 5': random_hand[4]})
