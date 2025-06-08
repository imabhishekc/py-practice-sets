"""
Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
*
**
***
if input is 4 then it should print

*
**
***
****
Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)
"""

# Solution 1
def print_pattern(lines):
    for i in range(1, lines + 1):
        print("*" * i)

print_pattern(5)


# Solution 2 (Alternate using two loops)
def print_pattern(lines):
    for i in range(1, lines + 1):
        for j in range(i):
            print("*", end="")
        print()

print_pattern(10)