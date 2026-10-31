
# Campus Event Seating and Entry Validation

rows = int(input("Enter number of rows: "))
seats_per_row = int(input("Enter seats per row: "))
capacity = rows * seats_per_row

seating = [
    [None for _ in range(seats_per_row)]
    for _ in range(rows)
]

n = int(input("Enter number of registered students: "))

if n < 0 or n > capacity:
    print("Error: Registered students must be between 0 and capacity.")
else:
    registered = []

    for i in range(n):
        student_id = input("Enter registration ID: ")

        while student_id in registered:
            print("This ID is already registered. Enter a unique ID.")
            student_id = input("Enter registration ID again: ")

        registered.append(student_id)

    # Assign seats row by row
    for i, student_id in enumerate(registered):
        row = i // seats_per_row
        seat = i % seats_per_row
        seating[row][seat] = student_id

    print("\n--- SEATING ARRANGEMENT ---")

    for i in range(rows):
        print("Row", i + 1, ":", seating[i])

    # Validate tickets at the entrance
    ticket_count = int(input("\nEnter number of tickets presented: "))
    entered = set()

    print("\n--- ENTRY VALIDATION ---")

    for i in range(ticket_count):
        ticket_id = input("Enter ticket registration ID: ")

        if ticket_id not in registered:
            print(ticket_id, "- INVALID TICKET")
        elif ticket_id in entered:
            print(ticket_id, "- DUPLICATE ENTRY")
        else:
            entered.add(ticket_id)
            print(ticket_id, "- VALID ENTRY")

    available = capacity - n

    print("\n--- EVENT REPORT ---")
    print("Total seating capacity:", capacity)
    print("Registered students:", n)
    print("Seats assigned:", n)
    print("Available seats:", available)
    print("Unique valid entries:", len(entered))
    print("Validation completed.")

