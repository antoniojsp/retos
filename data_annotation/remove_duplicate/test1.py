def remove_duplicates(lst):
    """Removes duplicates from a list and returns a new list.

    Args:
      lst: The input list.

    Returns:
      A new list with duplicates removed.
    """

    return list(set(lst))


my_list = [1, 2, 3, 4, 1, 2, 3, 4, 5]
unique_list = remove_duplicates(my_list)
print(unique_list)  # Output: [1, 2, 3, 4, 5]
