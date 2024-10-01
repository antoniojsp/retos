import tkinter as tk
from tkinter import messagebox, simpledialog
import google.generativeai as genai
import json

userdata = {
    'GOOGLE_API_KEY': 'AIzaSyCH4PvwOpskvrb8arY9Z3ZVxhFS1EsEW4Y' # Replace with your actual key
}

genai.configure(api_key=userdata['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')

# Initialize chat history; load from file if exists
try:
    with open("chat_history.json", "r") as f:
        chat_history = json.load(f)
        chat = model.start_chat(history=chat_history)
except FileNotFoundError:
    chat_history = []
    chat = model.start_chat(history=[])


def run_script():
    global chat_history
    user_input = simpledialog.askstring("Input", "What is your question?")
    if user_input:
        response = chat.send_message(user_input, stream=True)
        response_text = "\n".join([chunk.text for chunk in response])

        # Append to chat history
        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": response_text})

        messagebox.showinfo("Response", response_text)


def save_history():
    with open("chat_history.json", "w") as f:
        json.dump(chat_history, f, indent=4)  # Use indent for readability


root = tk.Tk()
root.title("Gemini Pro Chat")

send_button = tk.Button(root, text="Send Message", command=run_script)
send_button.pack(pady=20)

save_button = tk.Button(root, text="Save Conversation", command=save_history)
save_button.pack(pady=10)

root.mainloop()