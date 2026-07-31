s = input("Enter a string: ")

checked = ""

for ch in s:
    if ch not in checked:
        print(ch, ":", s.count(ch))
        checked += ch