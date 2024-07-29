import numpy as np

numbers = [-2, -8.1, -237, -1, -0.12]
closest_to_02 = min(numbers, key=lambda x: abs(x - 0.2))
print(closest_to_02)