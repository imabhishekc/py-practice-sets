"""
Ask user for a filename, read the file, and count how many lines it has. Handle errors.
"""

filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(f"The file has{len(lines)} lines.")
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print(f"Unexpected error occured {e}")
finally:
    print("File reading operation complete.")