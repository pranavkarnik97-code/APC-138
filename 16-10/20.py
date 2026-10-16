with open("transactions.txt", "w") as f:
    f.write("Deposit,5000\n")
    f.write("Withdrawal,-1000\n")
    f.write("Deposit,3000\n")
    f.write("Withdrawal,-500\n")

deposits = 0
withdrawals = 0
transactions = []

with open("transactions.txt", "r") as f:
    for line in f:
        name, amount = line.strip().split(",")
        amount = float(amount)
        transactions.append((name, amount))

        if amount > 0:
            deposits += amount
        else:
            withdrawals += abs(amount)

balance = deposits - withdrawals
largest = max(transactions, key=lambda x: abs(x[1]), default=None)

print("Total deposits:", deposits)
print("Total withdrawals:", withdrawals)
print("Final balance:", balance)

if largest:
    print("Largest transaction:", largest)