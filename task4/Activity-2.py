# Multi-Currency Travel Budget Analysis

expenses = []

budget = float(input("Enter total travel budget in INR: "))

n = int(input("Enter number of expense categories: "))

total_expenses = 0

for i in range(n):
    print("\nExpense Category", i + 1)

    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    currency = input("Enter currency code (USD/EUR/GBP): ").upper()
    rate = float(input("Enter exchange rate to INR: "))
    fee_percent = float(input("Enter conversion fee percentage: "))

    # Convert foreign currency into INR
    converted_amount = amount * rate

    # Calculate conversion fee
    fee = converted_amount * fee_percent / 100

    # Calculate final expense
    final_amount = converted_amount + fee

    # Store details in a tuple
    expense = (category, currency, amount, final_amount)
    expenses.append(expense)

    total_expenses += final_amount


# Find the largest expense category
largest_expense = expenses[0]

for expense in expenses:
    if expense[3] > largest_expense[3]:
        largest_expense = expense


# Display travel budget report
print("\n--- TRAVEL BUDGET REPORT ---")

for category, currency, amount, final_amount in expenses:
    print(category, ":", round(final_amount, 2), "INR")

print("Total Travel Expenses:", round(total_expenses, 2), "INR")
print("Travel Budget:", round(budget, 2), "INR")


# Compare expenses with budget
if total_expenses > budget:
    print("Status: Budget Exceeded")
    print("Extra Amount:", round(total_expenses - budget, 2), "INR")

elif total_expenses < budget:
    print("Status: Within Budget")
    print("Remaining Amount:", round(budget - total_expenses, 2), "INR")

else:
    print("Status: Budget Exactly Used")


print("Largest Expense Category:", largest_expense[0])
print("Largest Expense Amount:", round(largest_expense[3], 2), "INR")
