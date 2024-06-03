import tkinter as tk


def calculate_throughput():
    try:
        seats_per_train = int(seats_per_train_entry.get())
        cars_per_train = int(cars_per_train_entry.get())

        throughput = seats_per_train * cars_per_train

        result_label["text"] = f"Throughput: {throughput} passengers per train"
    except ValueError:
        result_label["text"] = "Please enter valid integer values."


def calculate_weight():
    try:
        seats_per_train = int(seats_per_train_entry.get())
        average_guest_weight = float(average_guest_weight_entry.get())
        average_car_weight = float(average_car_weight_entry.get())

        total_guest_weight = seats_per_train * average_guest_weight
        expected_car_weight = total_guest_weight + average_car_weight

        result_label["text"] = f"Expected Car Weight: {expected_car_weight:.2f} kg"
    except ValueError:
        result_label["text"] = "Please enter valid numeric values."


root = tk.Tk()
root.title("Rollercoaster Calculator")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Create labels and entries for seats per train, cars per train, average guest weight, and average car weight
tk.Label(frame, text="Seats per train:").grid(row=0, column=0)
seats_per_train_entry = tk.Entry(frame)
seats_per_train_entry.grid(row=0, column=1)

tk.Label(frame, text="Cars per train:").grid(row=1, column=0)
cars_per_train_entry = tk.Entry(frame)
cars_per_train_entry.grid(row=1, column=1)

tk.Label(frame, text="Average Guest Weight (kg):").grid(row=2, column=0)
average_guest_weight_entry = tk.Entry(frame)
average_guest_weight_entry.grid(row=2, column=1)

tk.Label(frame, text="Average Car Weight (kg):").grid(row=3, column=0)
average_car_weight_entry = tk.Entry(frame)
average_car_weight_entry.grid(row=3, column=1)

# Create buttons for calculation and a label to display the results
tk.Button(frame, text="Calculate Throughput", command=calculate_throughput).grid(row=4, columnspan=2)
tk.Button(frame, text="Calculate Weight", command=calculate_weight).grid(row=5, columnspan=2)

result_label = tk.Label(frame, text="")
result_label.grid(row=6, columnspan=2)

root.mainloop()