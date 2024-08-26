def equal_tuple_lengths(tuples_list):
    """Checks if all tuples in a list have equal length.

    Args:
      tuples_list: A list of tuples.

    Returns:
      True if all tuples have the same length, False otherwise.
    """

    if not tuples_list:
        return True  # Empty list is considered to have equal lengths

    first_tuple_length = len(tuples_list[0])
    return all(len(tuple) == first_tuple_length for tuple in tuples_list)


# Example usage:
tuples_list1 = [(11, 22, ), (44, 55, 66)]
tuples_list2 = [(11, 22,1), (44, 55, 66)]

print(equal_tuple_lengths(tuples_list1))  # Output: True
print(equal_tuple_lengths(tuples_list2))  # Output: False
