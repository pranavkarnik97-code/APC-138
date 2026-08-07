students = ["Amit", "Rahul", "Neha", "Priya"]

print("Total Students:", len(students))

name = input("Enter student name to search: ")

if name in students:
    print("Student Present")
else:
    print("Student Absent")

new = input("Enter new student name: ")
students.append(new)

remove = input("Enter absent student name: ")

if remove in students:
    students.remove(remove)

print("Updated Student List:")
print(students)