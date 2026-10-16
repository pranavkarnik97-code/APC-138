f = open("student.txt", "r")
text = f.read()
f.close()

old = input("Enter word to replace: ")
new = input("Enter new word: ")

text = text.replace(old, new)

f = open("student.txt", "w")
f.write(text)
f.close()

print("Text replaced successfully")