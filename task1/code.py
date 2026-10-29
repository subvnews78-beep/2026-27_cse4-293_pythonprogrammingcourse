
# University Scholarship Allocation System

students = []
eligible = []
ineligible = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Name: ")
    aggregate = float(input("Aggregate marks (%): "))

    print("Enter marks in 3 subjects:")
    m1 = float(input("Subject 1: "))
    m2 = float(input("Subject 2: "))
    m3 = float(input("Subject 3: "))

    attendance = float(input("Attendance (%): "))
    income = float(input("Annual family income (Rs.): "))

    reasons = []

    if aggregate < 75:
        reasons.append("Aggregate below 75%")

    if min(m1, m2, m3) < 60:
        reasons.append("Subject mark below 60%")

    if attendance < 75:
        reasons.append("Attendance below 75%")

    if income > 250000:
        reasons.append("Income above Rs. 250000")

    student = {
        "name": name,
        "aggregate": aggregate,
        "attendance": attendance,
        "income": income,
        "reasons": reasons
    }

    if len(reasons) == 0:
        eligible.append(student)
    else:
        ineligible.append(student)

# Sort by aggregate, attendance, income and name
eligible.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        s["name"].lower()
    )
)

print("\n--- ELIGIBLE STUDENTS ---")

if len(eligible) == 0:
    print("No eligible students.")
else:
    for rank, student in enumerate(eligible, start=1):
        print(
            rank, student["name"],
            "| Aggregate:", student["aggregate"], "%",
            "| Attendance:", student["attendance"], "%",
            "| Income: Rs.", student["income"]
        )

print("\n--- INELIGIBLE STUDENTS ---")

if len(ineligible) == 0:
    print("No ineligible students.")
else:
    for student in ineligible:
        print(student["name"], "-", ", ".join(student["reasons"]))

print("\nScholarship allocation process completed.")

