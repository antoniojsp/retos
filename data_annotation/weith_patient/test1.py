import matplotlib.pyplot as plt

# Create a list of patient identifiers
patient_identifiers = [12345, 45678, 78901, 90123, 10234]

# Create a list of weights
weights = [150, 200, 250, 175, 100]

# Create a list of follow-up times in months
followup_times = [12, 24, 36, 48, 60]

# Sort the data together by patient identifier
sorted_data = sorted(zip(patient_identifiers, weights, followup_times))
patient_identifiers, weights, followup_times = zip(*sorted_data)

# Create a time series plot
plt.figure(figsize=(10, 6))
for patient_identifier, weight, followup_time in zip(patient_identifiers, weights, followup_times):
    plt.plot(followup_time, weight, marker='o', label=f'Patient {patient_identifier}')

plt.xlabel('Follow-up Time (months)')
plt.ylabel('Body Weight (pounds)')
plt.title('Time Series of Patient Weight')
plt.legend()
plt.grid(True)
plt.show()