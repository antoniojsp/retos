def have_opposite_signs(x, y):
  """
  This function checks if two numbers have opposite signs.

  Args:
      x: The first number.
      y: The second number.

  Returns:
      True if the numbers have opposite signs, False otherwise.
  """

  # XOR of two numbers with opposite signs will be negative.
  # XOR of two numbers with the same sign will be positive or zero.
  return (x ^ y) < 0


