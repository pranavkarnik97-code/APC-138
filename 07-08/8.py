numbers = []

for i in range(5):
    n = int(input("Enter number: "))
    numbers.append(n)

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even)
print("Odd =", odd)