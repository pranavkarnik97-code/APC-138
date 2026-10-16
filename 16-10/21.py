def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")

    with open("books.txt", "a") as f:
        f.write(f"{book_id},{title},{author},Available\n")

    print("Book added")


def search_book():
    book_id = input("Enter book ID: ")

    try:
        with open("books.txt", "r") as f:
            for line in f:
                book = line.strip().split(",")
                if book[0] == book_id:
                    print(book)
                    return
        print("Book not found")
    except FileNotFoundError:
        print("No books available")


def change_status(book_id, status):
    try:
        with open("books.txt", "r") as f:
            books = [line.strip().split(",") for line in f]

        for book in books:
            if book[0] == book_id:
                if status == "Issued" and book[3] == "Available":
                    book[3] = "Issued"
                    break
                elif status == "Available" and book[3] == "Issued":
                    book[3] = "Available"
                    break
                else:
                    print("Operation not possible")
                    return
        else:
            print("Book not found")
            return

        with open("books.txt", "w") as f:
            for book in books:
                f.write(",".join(book) + "\n")

        print("Status updated")
    except FileNotFoundError:
        print("No books available")


def display_available():
    try:
        with open("books.txt", "r") as f:
            for line in f:
                book = line.strip().split(",")
                if book[3] == "Available":
                    print(book)
    except FileNotFoundError:
        print("No books available")


while True:
    print("\n1. Add book")
    print("2. Search book")
    print("3. Issue book")
    print("4. Return book")
    print("5. Display available books")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        change_status(input("Enter book ID: "), "Issued")
    elif choice == "4":
        change_status(input("Enter book ID: "), "Available")
    elif choice == "5":
        display_available()
    elif choice == "6":
        break
    else:
        print("Invalid choice")