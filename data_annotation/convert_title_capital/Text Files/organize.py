import os

# Set the root directory path
root_dir = '.'

# Define the file types and their corresponding subfolder names
file_types = {
    '.py': 'Text Files',
    '.jpg': 'Images',
    '.pdf': 'PDF Files'
}


# Function to sort files into subfolders
def sort_files_by_type(root_dir, file_types):
    # Loop through each file in the root directory
    for filename in os.listdir(root_dir):
        full_path = os.path.join(root_dir, filename)

        # Check if the file is a regular file
        if os.path.isfile(full_path):
            # Split the file extension from the filename
            ext = os.path.splitext(filename)[1].lower()

            # Check if the file extension is in our dictionary of file types
            if ext in file_types:
                subfolder_name = file_types[ext]
                subfolder_path = os.path.join(root_dir, subfolder_name)

                # Create the subfolder if it doesn't exist
                os.makedirs(subfolder_path, exist_ok=True)

                # Move the file to the corresponding subfolder
                destination_path = os.path.join(subfolder_path, filename)
                os.rename(full_path, destination_path)
                print(f"Moved {filename} to {subfolder_name}")


# Call the function to start sorting the files
sort_files_by_type(root_dir, file_types)

# User guide
print("User Guide:")
print("This script automatically sorts the files in the specified folder into subfolders based on their file type.")
print("To use it:")
print("1. Replace 'YOUR_CLUTTERED_FOLDER_PATH_HERE' with the actual path to the folder you want to sort.")
print("2. Make sure Python is installed on your computer.")
print("3. Save this script to a Python file (e.g., 'sort_files.py').")
print("4. Open a terminal or command prompt, navigate to the folder where the script is saved,")
print("5. Run the script by typing 'python sort_files.py' and press Enter.")
print("The script will create subfolders for the specified file types (.txt, .jpg, .pdf in this case)")
print(
    "and move the corresponding files into them. You can easily add more file types to be sorted by following the instructions below.")
print("To expand the script to include more file types:")
print("1. Add a new line in the 'file_types' dictionary, following the existing format:")
print("    file_types = { ..., '.YOUR_NEW_FILE_TYPE': 'YOUR_NEW_SUBFOLDER_NAME', ... }")
print(
    "2. That's it! Run the script again, and it will now sort files with the new file type into the corresponding subfolder.")
print("Remember to always replace 'YOUR_CLUTTERED_FOLDER_PATH_HERE' with the actual path to your folder.")
