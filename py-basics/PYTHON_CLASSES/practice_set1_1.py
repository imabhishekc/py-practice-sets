"""
Create a sample class named Employee with two attributes id and name
employee :
    id
    name
object initializes id and name dynamically for every Employee object created.

emp = Employee(1, "coder")
"""

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Create an object
emp = Employee(1, "coder")

print("Before deleting id:")
print("Employee ID: ", emp.id)
print("Employee Name: ", emp.name)

# Delete 'id' attribute
del emp.id

# Try accessing id now
print("\nAfter deleting 'id':")
try:
    print("Employee ID: ", emp.id)
except AttributeError:
    print("'id' attribute has been deleted.")

# Delet the entire object
del emp

# Try accessing object
print("\nAfter deleting object:")
try:
    print(emp.name)
except NameError:
    print("emp object no longer exists.")