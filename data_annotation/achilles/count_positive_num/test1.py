def count_positive_numbers(numbers):
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

# Test the function with the given list
numbers = [1, -2, 3, -4]
result = count_positive_numbers(numbers)
print(result)  # Output: 2