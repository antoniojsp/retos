import pandas as pd
import matplotlib.pyplot as plt

# Create a pandas dataframe
data = {
    "patient_identifier": [12345, 45678, 78901, 90123, 10234],
    "years_old": [25, 35, 45, 55, 65],
    "biological_sex": ["Female", "Male", "Male", "Female", "Male"],
    "body_weight_in_pounds": [150, 200, 250, 175, 100],
    "height_in_inches": [60, 72, 78, 66, 54],
    "body_mass_index": [25.0, 30.0, 35.0, 22.5, 18.5],
    "medical_case_identifier": [67890, 98765, 12345, 45678, 78901],
    "length_of_followup_in_months": [12, 24, 36, 48, 60],
    "clinical_diagnosis": ["Diabetes", "Heart Disease", "Cancer", "Asthma", "Alzheimer's Disease"]
}

df = pd.DataFrame(data)

# Plot time series of weight
plt.figure(figsize=(10, 6))
plt.plot(df["length_of_followup_in_months"], df["body_weight_in_pounds"], marker='o', linestyle='-')
plt.xlabel("Length of Followup (in months)")
plt.ylabel("Body Weight (in pounds)")
plt.title("Time Series of Patient Weight")
plt.grid(True)
plt.show()
