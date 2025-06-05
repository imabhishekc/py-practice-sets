"""
Write a program that prints following shape

*
**
***
****
*****
"""

# Solution 1
for i in range(1, 6):
    print("*" * i)


# Solution 2 using nested-loop
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()