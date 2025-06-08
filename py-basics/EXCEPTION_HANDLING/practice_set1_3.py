"""
Create a calculator that takes two inputs and an operator (+, -, *, /). 
Handle all invalid inputs (non-numeric, wrong operator, divide by zero).
"""
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+ or - or * or /): ")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = num1 / num2
    else:
        raise ValueError("Invalid operator.")
        
    print(f"Result: {result}")

# except ValueError as ve:
#     print("Value error:", ve)

# except ZeroDivisionError as zde:
#     print("Math Error:", zde)

finally:
    print("Calculation complete.")