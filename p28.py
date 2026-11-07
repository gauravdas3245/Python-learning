
def issue_book(books, book_name):
    if book_name in books:
        if books[book_name] > 0:
            books[book_name] -= 1
            print("Book issued successfully!")
        else:
            print("Book is out of stock!")
    else:
        print("Book not found!")


def return_book(books, book_name):
    if book_name in books:
        books[book_name] += 1
        print("Book returned successfully!")
    else:
        print("Book not found!")


books = {
    "Python": 3,
    "Java": 2,
    "C": 4
}

issue_book(books, "Python")
issue_book(books, "Python")

return_book(books, "Python")

print("Available Books:", books)
