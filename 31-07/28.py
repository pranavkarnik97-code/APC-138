s = input("Enter a paragraph: ")

words = s.lower().split()

freq = {}

for word in words:
    freq[word] = words.count(word)

for word in freq:
    print(word, ":", freq[word])