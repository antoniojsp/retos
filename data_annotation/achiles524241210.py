import cv2
import os

# Assuming you have a frame captured or provided as `frame`
# frame = ...

# Specify the folder name where you want to save the frame
folder_name = 'frames'

# Check if the folder exists, if not, create it
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Specify the path and name of the file you want to save
# For example, saving the image as frame1.png in the frames folder
file_name = os.path.join(folder_name, 'frame1.png')

# Save the frame as a .png image
cv2.imwrite(file_name, frame)

print(f'Frame saved as {file_name}')
