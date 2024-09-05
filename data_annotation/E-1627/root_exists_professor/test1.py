def check_integer_roots():
    # Define the range of x values to check
    for x in range(-100, 101):
        # Calculate y using the equation
        y = (x ** 3 - 7) / 9

        # Check if y is an integer
        print(x , y)
        if y == int(y):
            print(f"Integer root found: x = {x}, y = {int(y)}")
            return

    # If no integer roots are found, conclude that the professor is correct
    print("No integer roots found. The professor is correct.")


# Execute the function
check_integer_roots()