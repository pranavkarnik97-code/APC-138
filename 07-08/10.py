numbers = [10, 20, 30, 40, 50]

rev = []

for i in range(len(numbers)-1, -1, -1):
    rev.append(numbers[i])

print("Original List:", numbers)
print("Reversed List:", rev)