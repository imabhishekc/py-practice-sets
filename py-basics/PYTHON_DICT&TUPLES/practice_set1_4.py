"""
Write circle_calc() function that takes radius of a circle as an input 
from user and then it calculates and returns area, circumference and diameter. 
You should get these values in your main program by calling circle_calc function and then print them
"""

def circle_calc():
    radius = float(input("Enter the radius of the circle: "))

    # Calculating area
    area = 3.14 * radius**2
    diameter = 2 * radius
    circumference = 2 * 3.14 * radius
    return area, diameter, circumference

area, diameter, circumference = circle_calc()

print(f"Area: {area}")
print(f"Diameter: {diameter}")
print(f"Circumference: {circumference:.2f}")