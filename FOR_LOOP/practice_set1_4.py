"""
Lets say you are running a 5 km race. Write a program that,

Upon completing each 1 km asks you "are you tired?"
If you reply "yes" then it should break and print "you didn't finish the race"
If you reply "no" then it should continue and ask "are you tired" on every km
If you finish all 5 km then it should print congratulations message
"""

# Solution 1 using for loop
for km in range(1, 6):
    print(f"You have completed {km} km.")
    answer = input("Are you tired? (yes/no): ").strip().lower()

    if answer == "yes":
        print("You didn't finish the race.")
        break
else:
    print("Congratulations! You finished the race!")


# Solution 2 using while loop
km = 1

while km <= 5:
    print(f"You have completed {km} km.")
    answer = input("Are you tired? (yes/no): ").strip().lower()

    if answer == "yes":
        print("You didn't finish the race!")
        break
    
    km += 1
else:
    print("Congrtulations! You finished the race!")