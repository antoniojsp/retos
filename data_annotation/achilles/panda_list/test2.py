import pandas as pd


def remove_rows_by_list(df, column_name, value_list):
    """Removes rows from a DataFrame where a specified column contains values from a list.

    Args:
      df: The Pandas DataFrame.
      column_name: The name of the column to check.
      value_list: A list of values to filter out.

    Returns:
      A new DataFrame with the filtered rows removed.
    """

    return df[~df[column_name].isin(value_list)]


# Example usage
data = {'column1': [1, 2, 3, 4, 5],
        'column2': ['a', 'b', 'c', 'd', 'e']}
df = pd.DataFrame(data)

values_to_remove = [2, 4]

filtered_df = remove_rows_by_list(df, 'column1', values_to_remove)
print(filtered_df)
