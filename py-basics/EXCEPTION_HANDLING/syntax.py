"""
BASIC SYNTAX
try:
    # Code that might cause an error
except SomeError:
    # Code that runs if there's an error
"""

# EXAMPLE-1: Catching specific error
try:
    num = int(input("Enter a number: "))
    result = 10 /num
    print("Result:", result)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")


# EXAMPLE-2: Using 'finally'
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    print("This code block always runs.")


# EXAMPLE-3: Using 'else' clause
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("That's not a number!")
else:
    print(f"You are {age} years old.")