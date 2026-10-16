word = input("Enter word to search: ").lower()

f = open("student.txt", "r")
count = 0

for i, line in enumerate(f, start=1):
    words = line.lower().split()
    words = [w.strip(".,!?;:\"'()") for w in words]

    if word in words:
        print("Found on line:", i)
        count += words.count(word)

print("Total occurrences:", count)
f.close()