f = open("student.txt", "r")
words = f.read().lower().split()
f.close()

count = {}

for word in words:
    word = word.strip(".,!?;:\"'()")
    if word != "":
        count[word] = count.get(word, 0) + 1

print(count)