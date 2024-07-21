
body_weight_in_pounds = [150, 200, 250, 175, 100]
length_of_followup_in_months = [12, 24, 36, 48, 60]


import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.scatter(length_of_followup_in_months, body_weight_in_pounds, color='blue', marker='X', label='Patients')

plt.xlabel('Length of Follow-up')
plt.ylabel('Body Weight')
plt.title('Follow-up')

plt.grid(True)

plt.legend()
plt.tight_layout()
plt.show()