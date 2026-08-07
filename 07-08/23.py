numbers = [10, 20, 10, 30, 20, 10, 40, 30]

for i in numbers:
    if numbers.count(i) > 0:
        print(i, "=", numbers.count(i))
        while i in numbers:
            numbers.remove(i)