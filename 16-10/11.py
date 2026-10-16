f = open("student.txt", "r")
words = f.read().split()
f.close()

longest = ""

for word in words:
    word = word.strip(".,!?;:\"'()")
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)