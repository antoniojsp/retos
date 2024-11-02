import customtkinter as ctk
import requests
import tkinter.messagebox

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.default_fg_color = "#a87d32"  # White color for default state
        self.configure(fg_color=self.default_fg_color)
        self.geometry("400x200")
        self.title("Genderize")

        self.name_frame = ctk.CTkFrame(self)
        self.name_frame.pack(pady=20)

        self.name_label = ctk.CTkLabel(self.name_frame, text="Enter Name:")
        self.name_label.pack(side=ctk.LEFT, padx=(0, 10))

        self.name_entry = ctk.CTkEntry(self.name_frame, width=200)
        self.name_entry.pack(side=ctk.LEFT)

        self.button = ctk.CTkButton(self, text="Get Gender", command=self.get_gender, fg_color="green", hover_color="#2ECC40")
        self.button.pack(pady=20)

        self.gender_label = ctk.CTkLabel(self, text="")
        self.gender_label.pack(pady=(0, 20))

    def get_gender(self):
        name = self.name_entry.get()
        if not name.isalpha():
            tkinter.messagebox.showerror("Invalid Input", "Name should be alphabetic.")
            return

        response = self.call_api(name)
        if response:
            data = response.json()
            self.process_gender(data)

    def call_api(self, name):
        try:
            response = requests.get(f"https://api.genderize.io?name={name}")
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            tkinter.messagebox.showerror("API Error", f"An error occurred: {e}")
            return None

    def process_gender(self, data):
        gender = data.get('gender')
        probability = data.get('probability')

        if gender:
            if gender == 'male':
                self.configure(fg_color='#ADD8E6')  # light blue
            elif gender == 'female':
                self.configure(fg_color='#FFC0CB')  # light pink

            self.gender_label.configure(text=f"The likely gender of {self.name_entry.get()} is {gender} with a probability of {probability*100:.2f}%")
        else:
            self.gender_label.configure(text="Gender: Unknown")

if __name__ == "__main__":
    app = App()
    app.mainloop()