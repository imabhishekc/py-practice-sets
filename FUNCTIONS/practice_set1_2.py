"""
Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
rectangle area=length*width
If no shape is supplied then it should take triangle as a default shape
"""

def calculate_area(base, height, shape_type="triangle"):
    if shape_type == "rectangle":
        area = base * height  # base = length, height = length
    else:
        area = 1/2 * base * height
    return area

print("Area is:", calculate_area(2, 5, "rectangle"))
print("Area is:", calculate_area(2, 5)) # Default which is triangle