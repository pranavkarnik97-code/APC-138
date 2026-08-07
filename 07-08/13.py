numbers = []

for i in range(5):
    n = int(input("Enter number: "))
    numbers.append(n)

numbers.sort()
print("Ascending Order:", numbers)

numbers.sort(reverse=True)
print("Descending Order:", numbers)