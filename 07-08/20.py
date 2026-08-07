books = ["Python", "Java", "C++"]

new_book = input("Enter new book: ")
books.append(new_book)

search = input("Enter book to search: ")

if search in books:
    print("Book Found")
else:
    print("Book Not Found")

remove = input("Enter book to remove: ")

if remove in books:
    books.remove(remove)

print("Book List:")
for i in books:
    print(i)

print("Total Books:", len(books))