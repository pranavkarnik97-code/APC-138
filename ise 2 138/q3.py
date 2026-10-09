
filename = input("Enter the file name: ")
word = input("Enter the word to search: ")

try:
    with open(filename, "r") as file:
        text = file.read()

    words = text.split()
    frequency = sum(1 for w in words if w.strip(".,!?;:\"'()[]{}").lower() == word.lower())

    print("Frequency of", word, ":", frequency)

except FileNotFoundError:
    print("File not found!")