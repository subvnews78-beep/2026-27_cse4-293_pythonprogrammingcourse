
# Progressive Water Tariff Analysis

households = []
n = int(input("Enter number of households: "))

total_consumption = 0

for i in range(n):
    print("\nHousehold", i + 1)

    name = input("Enter household name or ID: ")
    units = float(input("Enter water consumption in units: "))

    # Calculate progressive water charges
    if units <= 100:
        charge = units * 2
    elif units <= 200:
        charge = (100 * 2) + (units - 100) * 3
    else:
        charge = (100 * 2) + (100 * 3) + (units - 200) * 5

    fixed_fee = 50
    penalty = 0

    if units > 200:
        penalty = 100

    bill = charge + fixed_fee + penalty

    if units > 200:
        status = "Excessive usage"
    else:
        status = "Normal usage"

    households.append({
        "name": name,
        "units": units,
        "charge": charge,
        "fixed": fixed_fee,
        "penalty": penalty,
        "bill": bill,
        "status": status
    })

    total_consumption += units

# Calculate average consumption
if n > 0:
    average = total_consumption / n
else:
    average = 0

print("\n--- WATER BILL REPORT ---")

for h in households:
    print("\nHousehold:", h["name"])
    print("Consumption:", h["units"], "units")
    print("Water charges: Rs.", round(h["charge"], 2))
    print("Fixed fee: Rs.", h["fixed"])
    print("Penalty: Rs.", h["penalty"])
    print("Total bill: Rs.", round(h["bill"], 2))
    print("Status:", h["status"])

print("\nTotal consumption:", total_consumption, "units")
print("Average consumption:", round(average, 2), "units")

print("\n--- EXCESSIVE USAGE REPORT ---")

found = False

for h in households:
    if h["units"] > 200:
        print(h["name"], "uses", h["units"], "units.")
        found = True

if not found:
    print("No household has excessive usage.")

print("\nWater tariff analysis completed.")

