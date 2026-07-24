n = int(input("Enter the value of N: "))
sum = 0
i = 1
while i <= n:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1

print("Sum of first", n, "even numbers is:", sum)
