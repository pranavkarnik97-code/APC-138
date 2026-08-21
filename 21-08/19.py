morning = {"Amit", "Rahul", "Priya", "Sneha"}
afternoon = {"Priya", "Sneha", "Rohan", "Kiran"}

print("Both sessions:", morning & afternoon)
print("Only morning:", morning - afternoon)
print("Only afternoon:", afternoon - morning)
print("At least one session:", morning | afternoon)