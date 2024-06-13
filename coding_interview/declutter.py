import os
import shutil

# Set the root folder path
root_folder_path = "PDF Files"

# Create a dictionary to store the file extensions and their corresponding subfolder paths
file_extensions_to_folders = {
    ".py": "PDF Files",
}

def create_subfolders(folder_paths):
    """
    This function creates the subfolders based on the provided list.
    """
    for folder_path in folder_paths:
        # Create the subfolder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

def sort_files_by_extension(folder_path):
    """
    This function sorts the files in the given folder based on their extension.
    """
    for filename in os.listdir(folder_path):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1].lower()

        # Check if the file extension matches any of the known extensions
        if file_extension in file_extensions_to_folders:
            # Get the corresponding subfolder path
            subfolder_path = file_extensions_to_folders[file_extension]

            # Move the file to the corresponding subfolder
            shutil.move(os.path.join(folder_path, filename), os.path.join(subfolder_path, filename))

# Main function
def main():
    # Create a list of subfolder paths based on the file extensions
    subfolder_paths = []
    for extension, folder_path in file_extensions_to_folders.items():
        subfolder_paths.append(os.path.join(root_folder_path, folder_path))

    # Create the subfolders if they don't exist
    create_subfolders(subfolder_paths)

    # Sort the files in each subfolder based on their extension
    sort_files_by_extension(root_folder_path)

    # Print a success message
    print("Files sorted successfully!")

if __name__ == "__main__":
    main()