def has_integer_root(equation, min_val, max_val):
    """
    Check if the given equation has an integer root within the specified range.

    Args:
        equation (str): The equation to be checked.
        min_val (int): The minimum value of x to check.
        max_val (int): The maximum value of x to check.

    Returns:
        bool: True if an integer root is found, False otherwise.
    """
    for x in range(min_val, max_val + 1):
        for y in range(min_val, max_val + 1):
            if eval(equation.replace('x', str(x)).replace('y', str(y))) == 0:
                print(f"Integer root found: x = {x}, y = {y}")
                return True
    return False


# Example usage
equation = "x**3 - 9*y - 7"
min_val = -100
max_val = 100

if has_integer_root(equation, min_val, max_val):
    print("The equation has an integer root within the specified range.")
else:
    print("The equation has no integer roots within the specified range.")
