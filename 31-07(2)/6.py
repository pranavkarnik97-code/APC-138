x = float(input("Enter x: "))
n = int(input("Enter highest even power: "))

sum = 1

for i in range(2, n + 1, 2):
    fact = 1
    for j in range(1, i + 1):
        fact *= j

    term = (x ** i) / fact

    if (i // 2) % 2 == 1:
        sum -= term
    else:
        sum += term

print("cos(x) =", sum)