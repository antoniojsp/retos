# Import the os module, which allows us to interact with the operating system
import os

# Define the directory you want to clean up
dir_path = "."

# Define a dictionary where the keys are file extensions and the values are the names of the folders you want to move them to
file_types = {
    "py": "Text Files",
    "jpg": "Images",
    "pdf": "PDFs"
}

# Loop over each file in the directory
for filename in os.listdir(dir_path):
    # Get the file extension
    file_ext = filename.split(".")[-1]

    # If the file extension is in our dictionary...
    if file_ext in file_types:
        # Build the full file path
        file_path = os.path.join(dir_path, filename)

        # Build the full destination folder path
        dest_folder_path = os.path.join(dir_path, file_types[file_ext])

        # If the destination folder doesn't exist, create it
        if not os.path.exists(dest_folder_path):
            os.makedirs(dest_folder_path)

        # Build the full destination file path
        dest_file_path = os.path.join(dest_folder_path, filename)

        # Move the file to the destination folder
        os.rename(file_path, dest_file_path)




# User Guide
# To use this script, simply replace "/path/to/your/directory" with the path to the directory you want to clean up.
# You can add more file types to the "file_types" dictionary. The key should be the file extension (without the leading dot)
# and the value should be the name of the folder you want to move files of that type to.
