f = open("student.txt", "r")
text = f.read()

print("Total characters:", len(text))
f.close()