import pandas as pd
import numpy as np

def map_cases_to_weights(cases, weights):
    """
    Maps cases dataframe to weights dataframe based on row-wise correspondence.

    Args:
        cases: Pandas DataFrame representing cases with unique rows.
        weights: Pandas DataFrame representing weights corresponding to each row in cases.

    Returns:
        Pandas DataFrame with weights mapped to each case.
    """

    cases_arr = cases.values
    weights_arr = weights.values

    # Create a dictionary to store unique case rows and their corresponding weight rows
    case_weight_map = {}
    for i in range(cases_arr.shape[0]):
        case_row = tuple(cases_arr[i])  # Convert to tuple for hashability
        case_weight_map[case_row] = weights_arr[i]


    # Create an array to store mapped weights
    mapped_weights = np.empty(cases_arr.shape)
    mapped_weights[:] = np.nan  # Initialize with NaN

    # Map weights to cases
    for i in range(cases_arr.shape[0]):
        case_row = tuple(cases_arr[i])
        if case_row in case_weight_map:
            mapped_weights[i] = case_weight_map[case_row]
    # Create a DataFrame from the mapped weights
    mapped_weights_df = pd.DataFrame(mapped_weights, columns=cases.columns)

    return mapped_weights_df

# Example usage:
cases = pd.DataFrame({"NAME": [1, 1, 1, 1, 1, 1, 1, 1, np.nan, np.nan, np.nan],
                      "citizenship_no": [1, np.nan, 1, 1, 1, np.nan, np.nan, np.nan, 1, np.nan, np.nan],
                      "Father_Name": [1, 1, np.nan, 1, np.nan, 1, np.nan, np.nan, np.nan, 1, np.nan],
                      "date_of_birth": [1, 1, 1, np.nan, np.nan, np.nan, 1, np.nan, np.nan, np.nan, 1]})
weights = pd.DataFrame({"NAME": [0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 1, np.nan, np.nan, np.nan],
                      "citizenship_no": [0.2, np.nan, 0.3, 0.3, 0.5, np.nan, np.nan, np.nan, 1, np.nan, np.nan],
                      "Father_Name": [0.2, 0.3, np.nan, 0.3, np.nan, 0.5, np.nan, np.nan, np.nan, 1, np.nan],
                      "date_of_birth": [0.2, 0.3, 0.3, np.nan, np.nan, np.nan, 0.5, np.nan, np.nan, np.nan, 1]})

mapped_weights_df = map_cases_to_weights(cases, weights)
print(mapped_weights_df)