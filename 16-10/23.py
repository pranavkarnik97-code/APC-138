with open("file1.txt", "r") as f:
    lines1 = f.readlines()

with open("file2.txt", "r") as f:
    lines2 = f.readlines()

same = True

for i in range(max(len(lines1), len(lines2))):
    line1 = lines1[i] if i < len(lines1) else None
    line2 = lines2[i] if i < len(lines2) else None

    if line1 != line2:
        print("Files are different")
        print("First difference at line:", i + 1)
        print("File 1:", line1)
        print("File 2:", line2)
        same = False
        break

if same:
    print("Files are identical")