import os 
import shutil

path = input("Enter the path of the folder you want to organize: ")
files = os.listdir(path)

for file in files:
    name, extension = os.path.splitext(file)
    extension = extension[1:]  # Remove the dot from the extension

    if extension:  # Check if the file has an extension
        new_folder = os.path.join(path, extension)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        shutil.move(os.path.join(path, file), os.path.join(new_folder, file))