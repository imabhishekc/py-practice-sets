max_number = int(input("Enter the maximum number you want up to: "))
odd_numbers = []
for i in range(1, max_number + 1):
    if i % 2 != 0:
        odd_numbers.append(i)

print(f"Odd numbers: {odd_numbers}")