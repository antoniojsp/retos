import traceback

try:
    from sympy import symbols, integrate, Eq, solve

    # Define the variables
    t = symbols('t')
    T = symbols('T')

    # Define the flow rate function
    f_t = t

    # Integrate the flow rate function from 0 to T
    volume = integrate(f_t, (t, 0, T))

    # Set the volume equal to 20000 gallons
    equation = Eq(volume, 20000)

    # Solve for T
    time_required = solve(equation, T)

    print(time_required)
except Exception as e:
    import traceback

    traceback.print_exc()