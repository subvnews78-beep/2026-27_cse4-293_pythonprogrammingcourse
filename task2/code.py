
# Progressive Electricity Billing System

months = []
bills = []

n = int(input("Enter number of months: "))

for i in range(n):
    print("\nMonth", i + 1)
    month = input("Enter month name: ")
    units = float(input("Enter units consumed: "))

    # Calculate progressive energy charges
    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = (100 * 2) + (units - 100) * 3
    else:
        energy = (100 * 2) + (100 * 3) + (units - 200) * 5

    fixed = 50
    surcharge = 0
    rebate = 0

    if units > 200:
        surcharge = energy * 0.05
    elif units <= 100:
        rebate = energy * 0.05

    total = energy + fixed + surcharge - rebate

    months.append(month)
    bills.append(total)

    print("Energy charges: Rs.", round(energy, 2))
    print("Fixed charges: Rs.", fixed)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Final bill: Rs.", round(total, 2))

# Compare consecutive months
print("\n--- MONTHLY BILL COMPARISON ---")

for i in range(n):
    print(months[i], "- Rs.", round(bills[i], 2))

    if i > 0:
        previous = bills[i - 1]
        current = bills[i]

        if previous > 0:
            increase = ((current - previous) / previous) * 100

            if increase > 30:
                print("ALERT: Unusual increase of",
                      round(increase, 2), "%")
            elif increase > 0:
                print("Bill increased by",
                      round(increase, 2), "%")
            elif increase < 0:
                print("Bill decreased by",
                      round(abs(increase), 2), "%")
            else:
                print("Bill unchanged.")

print("\nElectricity billing process completed.")

