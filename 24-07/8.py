age=int(input("Enter a age: "))
status=input("Enter a status: ")
gender=input("Enter a gender: ")
if status=="married":
    print("Driver insured")
elif gender=="female"and age>=25:
    print("Driver insured")
elif gender=="male" and age>=30:
    print("Driver insured")
else:
    print("Driver not insured")
