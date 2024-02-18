class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        if not books:
            print("There are no books available at the moment, try again later.")
        else:
            print("Books available in the library:")
            for book in books:
                book_info = book.strip().split(',')
                print(f"Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        release_year = input("Enter the release year of the book: ")
        num_pages = input("Enter the number of pages: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        new_books = []
        removed = False
        for book in books:
            if title not in book:
                new_books.append(book)
            else:
                removed = True
        if not removed:
            print("Book not found.")
        else:
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(new_books)
            print("Book removed successfully.")

lib = Library()
while True:
    print("***WELCOME TO OUR LIBRARY MANAGEMENT SYSTEM***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")

    choice = input("Please enter your choice: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 3.")
