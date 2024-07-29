def count_positive(numbers):
    """Counts the number of positive numbers in a list.

    Args:
      numbers: A list of numbers.

    Returns:
      The number of positive numbers in the list.
    """

    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count


numbers = [1, -2, 3, -4]
print(count_positive(numbers))  # Output: 2
