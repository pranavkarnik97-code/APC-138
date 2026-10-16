with open("attendance.txt", "w") as f:
    f.write("101,Amit,60,80\n")
    f.write("102,Priya,55,80\n")
    f.write("103,Rahul,70,80\n")

with open("attendance.txt", "r") as f:
    print("Students with attendance below 75%:")

    for line in f:
        roll, name, present, total = line.strip().split(",")
        percentage = int(present) / int(total) * 100

        print(name, "Attendance:", percentage, "%")

        if percentage < 75:
            print(name, "is below 75%")