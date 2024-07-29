def check_opposite_sign(x, y):
    """Checks if two numbers have opposite signs.

    Args:
      x: The first number.
      y: The second number.

    Returns:
      True if the numbers have opposite signs, False otherwise.
    """

    return x * y < 0


# Test the function with the given numbers
print(check_opposite_sign(-1, 2))  # Output: True
