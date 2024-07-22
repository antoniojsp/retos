# import pandas as pd
#
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
#
# # Read the CSV file into a DataFrame
# df = pd.read_csv('top_200_youtubers.csv')
#
# # Filter rows with null values in the 'Total Subscribers' column
# null_followers_df = df[df['Total Subscribers'].isnull()]
# if not null_followers_df.empty:
#     print(null_followers_df.to_string())
# else:
#     print("There are no records with null values in the 'Total Subscribers' column.")
# Total number of pieces
total_pieces = 1000

# Pieces placed by Poppy
placed_by_poppy = total_pieces * 1/4

# Remaining pieces after Poppy
remaining_after_poppy = total_pieces - placed_by_poppy

# Pieces placed by Mom (1/3 of remaining)
placed_by_mom = remaining_after_poppy * 1/3

# Pieces left to be placed
pieces_left = remaining_after_poppy - placed_by_mom

# Print the result
print(int(pieces_left))