numbers = [12,45,67,23,89,34,76]

largest = second = numbers[0]

for i in numbers:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second Largest Element:", second)