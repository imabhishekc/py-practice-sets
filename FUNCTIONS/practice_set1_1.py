"""
Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
area = (1/2)*base*height
"""

def calculate_area(base, height):
    area = 1/2 * base * height
    return area

result = calculate_area(12, 15)
print("Area of triangle:", result)