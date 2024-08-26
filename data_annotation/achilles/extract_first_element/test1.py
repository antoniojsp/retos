def extract_first_elements(lst):
  """Extracts the first element from each sublist in a list of lists.

  Args:
    lst: A list of lists.

  Returns:
    A list containing the first element of each sublist.
  """

  return [sublist[0] for sublist in lst]

# Example usage:
data = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
result = extract_first_elements(data)
print(result)  # Output: [1, 4, 7]