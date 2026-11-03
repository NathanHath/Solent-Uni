import os


def cwd():
    path = os.getcwd()
    files  = os.listdir(path)
    return path, files
current_path, current_files = cwd()
print(f"The current working directory is {current_path} \n The directory contains the following: {current_files} ")

