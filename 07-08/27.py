salary = []

n = int(input("Enter number of employees: "))

for i in range(n):
    salary.append(int(input("Enter Salary: ")))

highest = max(salary)
lowest = min(salary)
average = sum(salary) / len(salary)

above50 = 0
below30 = 0

for i in salary:
    if i > 50000:
        above50 += 1
    if i < 30000:
        below30 += 1

print("Highest Salary:", highest)
print("Lowest Salary:", lowest)
print("Average Salary:", average)
print("Employees Above ₹50000:", above50)
print("Employees Below ₹30000:", below30)