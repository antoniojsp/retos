import numpy as np
import pandas as pd

def map_cases_to_weights(cases, weights):
    # Convert DataFrames to NumPy arrays
    cases_array = cases.values
    weights_array = weights.values

    # Create a mapping dictionary
    mapping_dict = {tuple(case): weight for case, weight in zip(cases_array, weights_array)}

    # Vectorized function to map cases to weights
    vfunc = np.vectorize(lambda *args: mapping_dict.get(tuple(args), np.array([np.nan] * cases.shape[1])))

    # Apply the vectorized function to the cases array
    mapped_weights = vfunc(*[cases[col].values for col in cases.columns])

    # Convert the result back to a DataFrame
    result = pd.DataFrame(mapped_weights.T, columns=cases.columns, index=cases.index)

    return result

cases = pd.DataFrame({"NAME": [1, 1, 1, 1, 1, 1, 1, 1, np.nan, np.nan, np.nan],
                      "citizenship_no": [1, np.nan, 1, 1, 1, np.nan, np.nan, np.nan, 1, np.nan, np.nan],
                      "Father_Name": [1, 1, np.nan, 1, np.nan, 1, np.nan, np.nan, np.nan, 1, np.nan],
                      "date_of_birth": [1, 1, 1, np.nan, np.nan, np.nan, 1, np.nan, np.nan, np.nan, 1]})
weights = pd.DataFrame({"NAME": [0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 1, np.nan, np.nan, np.nan],
                      "citizenship_no": [0.2, np.nan, 0.3, 0.3, 0.5, np.nan, np.nan, np.nan, 1, np.nan, np.nan],
                      "Father_Name": [0.2, 0.3, np.nan, 0.3, np.nan, 0.5, np.nan, np.nan, np.nan, 1, np.nan],
                      "date_of_birth": [0.2, 0.3, 0.3, np.nan, np.nan, np.nan, 0.5, np.nan, np.nan, np.nan, 1]})


# Example usage
mapped_weights = map_cases_to_weights(cases, weights)
print(mapped_weights)