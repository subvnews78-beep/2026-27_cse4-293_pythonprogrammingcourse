# Comprehensive Smart Campus Management System

students = []
attendance = []
marks = []
events = []
resources = [("Projector", 5), ("Computers", 20),
             ("Smart Boards", 10)]

while True:

    print("\n===== SMART CAMPUS MANAGEMENT =====")
    print("1. Student Records")
    print("2. Attendance Management")
    print("3. Marks Management")
    print("4. Event Registration")
    print("5. Resource Allocation")
    print("6. Summary Report")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        branch = input("Enter Branch: ")

        students.append([sid, name, branch])
        print("Student record added successfully!")

    elif choice == "2":
        sid = input("Enter Student ID: ")
        present = int(input("Enter classes attended: "))
        total = int(input("Enter total classes: "))

        if total > 0 and 0 <= present <= total:
            percentage = (present / total) * 100
            attendance.append([sid, present, total, percentage])
            print("Attendance:", round(percentage, 2), "%")
        else:
            print("Invalid attendance details!")

    elif choice == "3":
        sid = input("Enter Student ID: ")
        m1 = int(input("Enter Python marks: "))
        m2 = int(input("Enter Maths marks: "))
        m3 = int(input("Enter Physics marks: "))

        if all(0 <= m <= 100 for m in [m1, m2, m3]):
            total = m1 + m2 + m3
            average = total / 3

            marks.append([sid, total, average])
            print("Total Marks:", total)
            print("Average:", round(average, 2))
        else:
            print("Invalid marks! Enter marks from 0 to 100.")

    elif choice == "4":
        sid = input("Enter Student ID: ")
        event = input("Enter Event Name: ")

        events.append((sid, event))
        print("Event registration successful!")

    elif choice == "5":
        print("\nAvailable Resources:")

        for resource, quantity in resources:
            print(resource, ":", quantity)

        name = input("Enter resource name: ")
        count = int(input("Enter required quantity: "))

        for i, (resource, quantity) in enumerate(resources):
            if resource.lower() == name.lower():
                if 0 < count <= quantity:
                    resources[i] = (resource, quantity - count)
                    print("Resource allocated successfully!")
                else:
                    print("Insufficient resource quantity!")
                break
        else:
            print("Resource not found!")

    elif choice == "6":
        print("\n===== CAMPUS SUMMARY REPORT =====")

        print("\nStudent Records:")
        for student in students:
            sid, name, branch = student
            print(sid, name, branch)

        print("\nAttendance Details:")
        for record in attendance:
            sid, present, total, percentage = record
            print(sid, round(percentage, 2), "%")

        print("\nMarks Details:")
        for record in marks:
            sid, total, average = record
            print(sid, total, round(average, 2))

        print("\nEvent Registrations:")
        for sid, event in events:
            print(sid, event)

        print("\nRemaining Resources:")
        for resource, quantity in resources:
            print(resource, quantity)

        print("\nTotal Students:", len(students))
        print("Total Attendance Records:", len(attendance))
        print("Total Event Registrations:", len(events))

    elif choice == "7":
        print("Thank you for using Smart Campus Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
