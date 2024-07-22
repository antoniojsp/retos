import tkinter as tk
from tkinter import font
import time


# Function to create the clock app
def create_clock_app():
    root = tk.Tk()
    root.title("Clock App")

    # Set the background color of root to orange
    root.configure(bg='orange')

    # Define a function to update the clock and date display
    def update_clock():
        # Get the current time and date
        current_time = time.strftime('%H:%M:%S', time.localtime())
        current_date = time.strftime('%b/%d/%Y', time.localtime()).upper()

        # Display the time in the time_label
        time_label['text'] = current_time
        # Display the date in the date_label
        date_label['text'] = current_date

        # Call the update_clock function every second to update the clock
        root.after(1000, update_clock)

    # Create a frame to hold the clock and date
    frame = tk.Frame(root, bg='white')
    frame.pack(padx=20, pady=20)

    # Create a font for the clock and date display
    clock_font = font.Font(family='Arial', size=40, weight='bold')

    # Create a label to display the time
    time_label = tk.Label(frame, bg='white', fg='orange', font=clock_font)
    time_label.grid(row=0, column=0)

    # Create a label to display the date
    date_font = font.Font(family='Arial', size=20, weight='bold')
    date_label = tk.Label(frame, bg='white', fg='orange', font=date_font)
    date_label.grid(row=1, column=0)

    # Start the clock update
    update_clock()

    # Run the main loop
    root.mainloop()


# Suggestion to extend the original clock
if __name__ == "_main_":
    # Set the desired timezone (UTC +5 is used as an example)
    # You can learn more about timezones in Python with 'pytz' module
    time.tzset('UTC+5')

    # Call the create_clock_app function to start the application
    create_clock_app()