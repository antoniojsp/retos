import matplotlib.pyplot as plt

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

values = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]  # Example values



plt.figure(figsize=(10, 10))
plt.pie(values, labels=months)

plt.title('Budget per month in 2024')

plt.show()