employees = [
    ["101", "Amit", "IT", 50000],
    ["102", "Priya", "HR", 60000],
    ["103", "Rahul", "Sales", 40000]
]

with open("employees.txt", "w") as f:
    for e in employees:
        f.write(",".join(map(str, e)) + "\n")


def read_employees():
    data = []
    with open("employees.txt", "r") as f:
        for line in f:
            emp_id, name, dept, salary = line.strip().split(",")
            data.append([emp_id, name, dept, float(salary)])
    return data


def display_employees():
    for e in read_employees():
        print(e)


def highest_paid():
    e = max(read_employees(), key=lambda x: x[3])
    print("Highest paid:", e[1], e[3])


def average_salary():
    data = read_employees()
    avg = sum(e[3] for e in data) / len(data)
    print("Average salary:", avg)


def above_salary(amount):
    for e in read_employees():
        if e[3] > amount:
            print(e)


display_employees()
highest_paid()
average_salary()
above_salary(float(input("Enter salary: ")))