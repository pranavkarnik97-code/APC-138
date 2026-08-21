employee1 = {"Python", "Java", "SQL", "HTML"}
employee2 = {"Python", "C++", "SQL", "CSS"}

print("Common skills:", employee1 & employee2)
print("Employee 1 unique:", employee1 - employee2)
print("Employee 2 unique:", employee2 - employee1)
print("All skills:", employee1 | employee2)