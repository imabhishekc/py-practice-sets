try:
    sugar_level = float(input("Enter your fasting sugar level: "))

    if sugar_level < 80:
        print("Your sugar level is low.") 
    elif sugar_level > 100:
        print("Your sugar level is high.")
    else:
        print("Your sugar level is normal.")
        
except ValueError:
    print("Invalid input. Please enter a number.")