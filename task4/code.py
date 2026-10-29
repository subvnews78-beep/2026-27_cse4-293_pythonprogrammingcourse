
# Student Timetable Conflict Detection

schedules = []

n = int(input("Enter number of classes: "))

for i in range(n):
    print("\nClass", i + 1)

    course = input("Enter course name: ")
    day = input("Enter day: ").lower()
    start = input("Enter start time (HH:MM): ")
    end = input("Enter end time (HH:MM): ")
    room = input("Enter room number: ").upper()

    # Store schedule details in a tuple
    schedule = (course, day, start, end, room)
    schedules.append(schedule)


# Convert HH:MM string into minutes
def to_minutes(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes


conflicts = []
room_conflicts = []

for i in range(n):
    for j in range(i + 1, n):

        c1, d1, s1, e1, r1 = schedules[i]
        c2, d2, s2, e2, r2 = schedules[j]

        # Compare classes on the same day
        if d1 == d2:
            start1 = to_minutes(s1)
            end1 = to_minutes(e1)
            start2 = to_minutes(s2)
            end2 = to_minutes(e2)

            # Check overlapping periods
            if start1 < end2 and start2 < end1:
                conflicts.append((c1, c2))
                print("\nTimetable conflict:", c1, "and", c2)

                # Check whether the room is the same
                if r1 == r2:
                    room_conflicts.append((c1, c2, r1))
                    print("Room", r1, "is unavailable for both classes.")


print("\n--- TIMETABLE VALIDATION ---")

if len(conflicts) == 0:
    print("No overlapping classes found.")
else:
    print("Total timetable conflicts:", len(conflicts))

if len(room_conflicts) == 0:
    print("No room conflicts found.")
else:
    print("Total room conflicts:", len(room_conflicts))

if len(conflicts) == 0 and len(room_conflicts) == 0:
    print("Proposed timetable is VALID.")
else:
    print("Proposed timetable is INVALID.")

