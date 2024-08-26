cases = pd.DataFrame({"NAME": [1, 1, 1, 1, 1, 1, 1, 1, np.nan, np.nan, np.nan],\
                      "citizenship_no": [1, np.nan, 1, 1, 1, np.nan, np.nan, np.nan, 1, np.nan, np.nan],
                      "Father_Name": [1, 1, np.nan, 1, np.nan, 1, np.nan, np.nan, np.nan, 1, np.nan],
                      "date_of_birth": [1, 1, 1, np.nan, np.nan, np.nan, 1, np.nan, np.nan, np.nan, 1]})
weights = pd.DataFrame({"NAME": [0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 1, np.nan, np.nan, np.nan],\
                      "citizenship_no": [0.2, np.nan, 0.3, 0.3, 0.5, np.nan, np.nan, np.nan, 1, np.nan, np.nan],
                      "Father_Name": [0.2, 0.3, np.nan, 0.3, np.nan, 0.5, np.nan, np.nan, np.nan, 1, np.nan],
                      "date_of_birth": [0.2, 0.3, 0.3, np.nan, np.nan, np.nan, 0.5, np.nan, np.nan, np.nan, 1]})