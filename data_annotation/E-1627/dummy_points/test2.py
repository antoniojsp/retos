import numpy as np
import pandas as pd
import traceback


def generate_dummy_dataset(slope, intercept, std_dev, num_points):
    try:
        # Generate random X values
        X = np.random.rand(num_points) * 100  # Random values between 0 and 100

        # Generate Y values based on the linear equation Y = MX + B with added noise
        noise = np.random.normal(0, std_dev, num_points)
        Y = slope * X + intercept + noise

        # Create a DataFrame
        data = pd.DataFrame({'X': X, 'Y': Y})

        return data
    except Exception as e:
        traceback.print_exc()


# Example usage
slope = 2
intercept = 40
std_dev = 10
num_points = 50

try:
    dummy_data = generate_dummy_dataset(slope, intercept, std_dev, num_points)
    print(dummy_data)
except Exception as e:
    traceback.print_exc()
