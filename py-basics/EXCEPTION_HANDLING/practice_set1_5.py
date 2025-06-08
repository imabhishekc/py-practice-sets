"""
Custom Exceptions,
You can even define your own exception:
class TooSmallError(Exception):
    pass

Write a program that raises TooSmallError if the input number is less than 10.
"""

# Create a custom Exception class inheriting the python's Exception class
class TooSmallError(Exception):
    """Custom exception raised when the number is less than 10."""
    pass

try:
    num = int(input("Enter a number (>=10): "))
    if num < 10:
        raise TooSmallError("Number is too small! It should be 10 or greater than 10.")
    print("You entered: ", num)

except TooSmallError as e:
    print(e)

except ValueError:
    print("Please enter a valid number.")

finally:
    print("Input check complete.")