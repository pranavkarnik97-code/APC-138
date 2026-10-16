f1 = open("file1.txt", "r")
text1 = f1.read()
f1.close()

f2 = open("file2.txt", "r")
text2 = f2.read()
f2.close()

f3 = open("file3.txt", "w")
f3.write(text1)

if text1 and text2 and not text1.endswith("\n"):
    f3.write("\n")

f3.write(text2)
f3.close()

print("Both files combined into file3.txt")