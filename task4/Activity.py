
# Multi-Currency Travel Budget Analysis

budget = float(input("Enter travel budget in INR: "))
n = int(input("Enter number of expenses: "))

expenses = []
category_totals = {}
total_spending = 0

for i in range(n):
    print("\nExpense", i + 1)

    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))
    currency = input("Enter currency code: ").upper()
    rate = float(input("Enter exchange rate to INR: "))

    # Convert expense into INR
    converted = amount * rate

    # Calculate 2% conversion fee
    fee = converted * 0.02

    # Final expense including fee
    final_amount = converted + fee

    expenses.append({
        "category": category,
        "currency": currency,
        "amount": amount,
        "converted": converted,
        "fee": fee,
        "total": final_amount
    })

    category_totals[category] = (
        category_totals.get(category, 0) + final_amount
    )

    total_spending += final_amount

# Display expense details
print("\n--- TRAVEL EXPENSE REPORT ---")

for expense in expenses:
    print("\nCategory:", expense["category"])
    print("Original amount:", expense["amount"],
          expense["currency"])
    print("Converted amount: Rs.",
          round(expense["converted"], 2))
    print("Conversion fee: Rs.",
          round(expense["fee"], 2))
    print("Final expense: Rs.",
          round(expense["total"], 2))

print("\nTotal spending: Rs.", round(total_spending, 2))
print("Planned budget: Rs.", round(budget, 2))

# Compare spending with budget
if total_spending > budget:
    print("Budget exceeded by Rs.",
          round(total_spending - budget, 2))
elif total_spending < budget:
    print("Budget remaining: Rs.",
          round(budget - total_spending, 2))
else:
    print("Budget used completely.")

# Find largest expense category
if category_totals:
    largest = max(category_totals, key=category_totals.get)

    print("\n--- CATEGORY SUMMARY ---")

    for category, amount in category_totals.items():
        print(category, ": Rs.", round(amount, 2))

    print("Largest expense category:", largest)
    print("Amount: Rs.", round(category_totals[largest], 2))

print("\nTravel budget analysis completed.")

