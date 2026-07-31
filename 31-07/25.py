s = input("Enter a string: ")

freq = {}

for ch in s:
    freq[ch] = s.count(ch)

items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

if len(items) >= 2:
    print("Second Most Frequent Character:", items[1][0])
    print("Frequency:", items[1][1])
else:
    print("No second most frequent character.")