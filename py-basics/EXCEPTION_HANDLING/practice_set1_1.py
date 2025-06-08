"""
Take input from user and divide 100 by it. Handle ZeroDivisionError and ValueError.
"""

number = int(input("Enter the number: "))

try:
    div = 100 / number
    print(f"Result: {div}")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Invalid input! Please input non zero number.")
