"""
Create a program that will access my one drive folder and change the file extension of all the images in the folder to .jpg
and delete the original file with the old extension.
"""

import os
import shutil
import uuid


# Path to the folder containing the images
path = r"D:\SecurityCams"

# List of all the files in the folder
files = os.listdir(path)

# Loop through all the files in the folder
for file in files:
    # Check if the file is an image
    if file.endswith((".png", ".jpeg", ".gif", ".bmp", ".tiff", ".heic")):
        # Get the file name without the extension
        file_name = os.path.splitext(file)[0]
        # New file name
        new_file_name = os.path.join(path, file_name + ".jpg")
        # Check if file already exists
        if os.path.exists(new_file_name):
            # Append a unique identifier to the file name
            new_file_name = os.path.join(path, file_name + "_" + str(uuid.uuid4()) + ".jpg")
        # Rename the file with the new extension
        os.rename(os.path.join(path, file), new_file_name)

        
        







