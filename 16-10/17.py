import csv

records = [
    ["RollNo", "Name", "Marks"],
    [101, "Amit", 85],
    [102, "Priya", 92],
    [103, "Rahul", 78]
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(records)

with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    students = list(reader)

print("All student records:")
for s in students:
    print(s["RollNo"], s["Name"], s["Marks"])

highest = max(students, key=lambda s: int(s["Marks"]))
print("Highest marks:", highest["Name"], highest["Marks"])

average = sum(int(s["Marks"]) for s in students) / len(students)
print("Average marks:", average)

print("Students scoring more than 80:")
for s in students:
    if int(s["Marks"]) > 80:
        print(s["Name"], s["Marks"])