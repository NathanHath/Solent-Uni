import os

def display_chars(file_path, num_chars ):
    with open (file_path, mode='r') as f:
        read = f.read(num_chars)
    return read

def display_line(file_path):
    with open (file_path, mode='r') as f:
        all_lines = f.readlines()
        read = all_lines[3]
    return read

def display_text(file_path):
    with open (file_path, mode='r') as f:
        read = f.read().strip()
    return read

def run_task2():
    file_path = "liberary"
    print (display_chars(file_path, 1))
    print (display_line(file_path))
    print (display_text(file_path))

run_task2()