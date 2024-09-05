import pandas as pd
import numpy as np


def generate_dummy_dataset(M, B, std_dev, n):
    # Generate n random X values
    X = np.random.uniform(0, 10, n)

    # Calculate Y values with added noise
    Y = M * X + B + np.random.normal(0, std_dev, n)

    # Create a DataFrame
    df = pd.DataFrame({'X': X, 'Y': Y})

    return df


# Example usage:
M = 2  # Slope
B = 30  # Intercept
std_dev =30# Standard deviation
n = 10  # Number of data points

dummy_dataset = generate_dummy_dataset(M, B, std_dev, n)
print(dummy_dataset)