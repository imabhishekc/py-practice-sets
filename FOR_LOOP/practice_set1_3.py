"""
Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.
"""

# Solution 1
expense_list = [2340, 2500, 2100, 3100, 2980]
expense_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May']


expense_amount = int(input("Enter an expense amount: "))

found = False
for i in range(len(expense_list)):
    if expense_list[i] == expense_amount:
        print(f"Expense of {expense_amount} occured in {expense_month[i]}")
        found = True

if not found:
    print("Expense not found.")


# Solution 2
expense_list = [2340, 2500, 2100, 3100, 2980]
expense_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

expense_amount = int(input("Enter an expense amount: "))

for month, amount in zip(expense_month, expense_list):
    if amount == expense_amount:
        print(f"Expense of {expense_amount} occured in {month}")
        break

else:
    print("Expense not found.")