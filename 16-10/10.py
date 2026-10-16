f = open("student.txt", "r")
text = f.read()

alphabets = 0
digits = 0
spaces = 0
special = 0

for ch in text:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    elif ch != "\n" and ch != "\t":
        special += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

f.close()