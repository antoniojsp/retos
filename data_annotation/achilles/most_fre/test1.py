from collections import Counter

def find_most_frequent_strings(strings):
  """Finds the 3 most frequent strings in a list of strings.

  Args:
    strings: A list of strings.

  Returns:
    A list of tuples, where each tuple contains a string and its frequency.
    The list is sorted by frequency in descending order.
  """

  # Count the occurrences of each string
  string_counts = Counter(strings)

  # Get the 3 most frequent strings
  most_frequent = string_counts.most_common(3)

  return most_frequent

# Example usage
strings = ['abc', 'def', 'abc', 'def', 'a', 'h', 'dfdfd', 'dfdfd', 'abc', 'dfdfd', 'dfdfd']
most_frequent_strings = find_most_frequent_strings(strings)
print(most_frequent_strings)