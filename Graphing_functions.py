#%% Working with the data(all hand ranks)
#
#
#

# Builds two dataframes (rank count [rc] and card occurrence [co] from an existing data set)
expected_rc_df = pd.read_excel('Data/Expected poker hand outcomes.xlsx', sheet_name='Ranks')
expected_co_df = pd.read_excel('Data/Expected poker hand outcomes.xlsx', sheet_name='Cards')

# Builds a dataframe from an existing sample of 1 million poker hands simulated using this code
million_hand_df = pd.read_excel('Data/Poker Hand Statistics 1mil.xlsx')

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
plt.show()


# Hands drawn time comparison of with image and without
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
plt.title('Poker Hand Simulator: Runtime vs. Hand #', fontsize=14)

plt.show()
