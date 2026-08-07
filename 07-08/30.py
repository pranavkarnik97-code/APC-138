patients = ["Amit", "Rahul", "Neha"]
ages = [25, 30, 22]

name = input("Enter New Patient Name: ")
age = int(input("Enter Age: "))

patients.append(name)
ages.append(age)

search = input("Enter Patient Name to Search: ")

if search in patients:
    index = patients.index(search)
    print("Patient:", patients[index])
    print("Age:", ages[index])
else:
    print("Patient Not Found")

delete = input("Enter Patient Name to Delete: ")

if delete in patients:
    index = patients.index(delete)
    patients.pop(index)
    ages.pop(index)

print("\nPatient Details:")
for i in range(len(patients)):
    print(patients[i], "-", ages[i])

print("Total Patients:", len(patients))