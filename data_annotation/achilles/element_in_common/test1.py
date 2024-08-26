def find_common_elements(lists):
    """Finds common elements in a list of lists.

    Args:
      lists: A list of lists of numbers.

    Returns:
      A list of common elements.
    """

    if not lists:
        return []

    # Convert lists to sets for efficient intersection
    sets = [set(lst) for lst in lists]

    # Find the intersection of all sets
    common_elements = sets[0].intersection(*sets[1:])

    return list(common_elements)


# Example usage
lists = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
common_elements = find_common_elements(lists)
print(common_elements)  # Output: [12, 18]
