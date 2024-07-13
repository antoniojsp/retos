
import tkinter as tk
from tkinter import font
import time
# Define the function to create the clock app
def create_clock_app():
    # Create the main window
    root = tk.Tk()
    root.title("Clock App")

    # Create a frame to hold the clock and date labels
    frame = tk.Frame(root, bg="orange")
    frame.pack(padx=20, pady=20)

    # Create a label to display the current time
    time_label = tk.Label(frame, font=("Helvetica", 48), fg="white", bg="orange")
    time_label.pack(padx=10, pady=10)

    # Create a label to display the current date
    date_label = tk.Label(frame, font=("Helvetica", 24), fg="white", bg="orange")
    date_label.pack(padx=10, pady=10)

    # Function to update the clock and date labels
    def update_clock():
        current_time = time.strftime("%H:%M:%S")
        time_label["text"] = current_time

        current_date = time.strftime("%m/%d/%Y")
        date_label["text"] = current_date

        # Call the update_clock function again after 1 second
        root.after(1000, update_clock)

    # Start the clock update loop
    update_clock()

    # Set the window size to fit the contents
    root.geometry("300x150")

    # Start the main loop
    root.mainloop()

# Call the function to create the clock app
create_clock_app()