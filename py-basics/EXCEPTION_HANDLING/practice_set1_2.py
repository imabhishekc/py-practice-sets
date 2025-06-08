"""
Try to open a file called notes.txt. If the file doesn't exist, handle it gracefully.
"""

try:
    with open("notes.txt", "r") as file:
        view_file = file.read()
        print(view_file)
except FileNotFoundError:
    print("The file you're trying to open does not exist.")
finally:
    print("File handling operation is complete.")