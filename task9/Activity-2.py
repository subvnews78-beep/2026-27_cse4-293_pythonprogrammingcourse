
# Smart Public Transport Fare Reconciliation

fares = {
    "Adult": 30,
    "Student": 15,
    "Senior Citizen": 20,
    "Child": 10
}

routes = int(input("Enter number of routes: "))

total_expected = 0
total_collected = 0

print("\n--- FARE RECONCILIATION REPORT ---")

for i in range(routes):
    print("\nRoute", i + 1)

    route_name = input("Enter route name: ")
    route_expected = 0

    for category, fare in fares.items():
        count = int(input("Enter number of " + category + " passengers: "))
        route_expected += count * fare

    collected = float(input("Enter collected revenue: "))

    discrepancy = collected - route_expected

    total_expected += route_expected
    total_collected += collected

    print("\nRoute:", route_name)
    print("Expected revenue: Rs.", round(route_expected, 2))
    print("Collected revenue: Rs.", round(collected, 2))
    print("Discrepancy: Rs.", round(discrepancy, 2))

    if discrepancy > 0:
        print("Status: Excess collection")
    elif discrepancy < 0:
        print("Status: Revenue shortage")
    else:
        print("Status: Reconciled")

overall_difference = total_collected - total_expected

print("\n--- OVERALL SUMMARY ---")
print("Total expected revenue: Rs.", round(total_expected, 2))
print("Total collected revenue: Rs.", round(total_collected, 2))
print("Overall discrepancy: Rs.", round(overall_difference, 2))

if overall_difference > 0:
    print("Overall status: Excess collection")
elif overall_difference < 0:
    print("Overall status: Revenue shortage")
else:
    print("Overall status: Fully reconciled")

print("Reconciliation completed.")

