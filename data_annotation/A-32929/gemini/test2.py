userdata = {
    'GOOGLE_API_KEY': 'AIzaSyCH4PvwOpskvrb8arY9Z3ZVxhFS1EsEW4Y'
}

import tkinter as tk
from tkinter import messagebox, simpledialog
import json

import google.generativeai as genai

# Configure the Google API
genai.configure(api_key=userdata['GOOGLE_API_KEY'])

# Initialize the model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# List to store the conversation history
conversation_history = []


def run_script():
    global conversation_history

    # Ask for input using a dialog
    user_input = simpledialog.askstring("Input", "What is your question?")
    if user_input:  # Proceed only if user provided input
        response = chat.send_message(user_input, stream=True)
        response_text = "\n".join([chunk.text for chunk in response])

        # Add the user input and response to conversation history
        conversation_history.append({'user_input': user_input, 'response_text': response_text})

        messagebox.showinfo("Response", response_text)


def save_conversation():
    global conversation_history

    # Save conversation history to a JSON file
    with open("conversation_history.json", "w") as file:
        json.dump(conversation_history, file, indent=4)
    messagebox.showinfo("Save", "Conversation history saved successfully!")


# Create the main window
root = tk.Tk()
root.title("Gemini Pro Chat")

# Create a button to send a message
send_button = tk.Button(root, text="Send Message", command=run_script)
send_button.pack(pady=20)

# Create a button to save the conversation
save_button = tk.Button(root, text="Save Conversation", command=save_conversation)
save_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()