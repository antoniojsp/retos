import customtkinter as ctk
import requests
import tkinter.messagebox

# Constants
DEFAULT_FG_COLOR = "#FFFFFF"  # White
ERROR_COLOR = "#FF6347"  # Tomato
SUCCESS_COLOR_MALE = "#ADD8E6"  # Light Blue
SUCCESS_COLOR_FEMALE = "#FFC0CB"  # Light Pink
API_URL = "https://api.genderize.io"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Genderize")
        self.geometry("400x200")
        self.configure(fg_color=DEFAULT_FG_COLOR)

        self.name_frame = self.create_name_frame()
        self.name_frame.pack(pady=20)

        self.gender_label = ctk.CTkLabel(self, text="")
        self.gender_label.pack(pady=(0, 20))

        self.button = ctk.CTkButton(self, text="Get Gender", command=self.get_gender, fg_color="green", hover_color="#2ECC40")
        self.button.pack(pady=20)

    def create_name_frame(self):
        frame = ctk.CTkFrame(self)
        label = ctk.CTkLabel(frame, text="Enter Name:")
        label.pack(side=ctk.LEFT, padx=(0, 10))

        entry = ctk.CTkEntry(frame, width=200)
        entry.pack(side=ctk.LEFT)
        return frame

    def configure_app(self, fg_color):
        self.configure(fg_color=fg_color)
        self.name_frame.configure(fg_color=fg_color)
        self.gender_label.configure(fg_color=fg_color)
        self.button.configure(fg_color=fg_color)

    def get_gender(self):
        name = self.name_frame.name_entry.get()
        if not name.isalpha():
            tkinter.messagebox.showerror("Invalid Input", "Name should be alphabetic.")
            self.configure_app(ERROR_COLOR)
            return

        try:
            response = requests.get(f"{API_URL}?name={name}")
            data = response.json()
            self.update_gender_label(data)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"An error occurred: {e}")
            self.configure_app(ERROR_COLOR)

    def update_gender_label(self, data):
        gender = data.get('gender')
        probability = data.get('probability')

        if gender:
            if gender == 'male':
                self.configure_app(SUCCESS_COLOR_MALE)
            elif gender == 'female':
                self.configure_app(SUCCESS_COLOR_FEMALE)

            self.gender_label.configure(text=f"The likely gender of {name} is {gender} with a probability of {probability*100:.2f}%")
        else:
            self.configure_app(DEFAULT_FG_COLOR)
            self.gender_label.configure(text="Gender: Unknown")

if __name__ == "__main__":
    app = App()
    app.mainloop()