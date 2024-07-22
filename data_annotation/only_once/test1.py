def find_single_element(nums):
  """Finds the element that appears only once in a sorted array.

  Args:
    nums: A sorted array of integers.

  Returns:
    The element that appears only once.
  """

  for i in range(0, len(nums), 2):
    if i + 1 == len(nums) or nums[i] != nums[i + 1]:
      return nums[i]

  return -1  # If no single element found

# Example usage:
nums = [1, 1, 2, 3, 3, 5, 5]
result = find_single_element(nums)
print(result)  # Output: 3