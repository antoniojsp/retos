def filter_and_sort_even_numbers(numbers):

    return sorted([num for num in numbers if num % 2 == 0])


# Example usage:

print(filter_and_sort_even_numbers([5, 2, 9, 4, 1, 8]))  # Output: [2, 4, 8]
