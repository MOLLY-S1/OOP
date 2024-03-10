class Books:
    def __init__(self, title, author, dewy, isbn):
        self.title = title.title()
        self.author = author
        self.dewy = dewy
        self.isbn = isbn
        self.available = True
        self.borrower = None
        book_list.append(self)  # adding book objects created in main routine to full book list

    def book_details(self):
        print(self.title)
        print(self.author)
        print(self.dewy)
        print(self.isbn)
        print(self.available)
        print(self.borrower)
        print("########################")


def print_info():
    for book in book_list:
        book.book_details()


class Users:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.fees = 0.0
        self.borrowed = []
        user_list.append(self)

    def user_details(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Fees: ${self.fees}")
        print("########################")


def print_user_info():
    for user in user_list:
        user.user_details()


def add_user():
    name = input("Enter Name: ").title()
    address = input("Enter Address: ")
    Users(name, address)
    print(name, address, "has been added to users")


def find_user():
    user_to_find = input("Enter Name: ").title()
    for user in user_list:
        if user.name == user_to_find:
            print(f"User {user.name} found")
            return user
    print(f"Sorry, no user was found called {user_to_find}")
    return None


def add_book():
    title = input("Enter title: ").title()
    author = input("Enter Author: ").title()
    dewy = input("Enter Dewy: ")
    isbn = input("Enter ISBN: ")
    Books(title, author, dewy, isbn)
    print(f"Book {title} has been added")


def find_book():
    book_to_find = input("Enter title: ").title()
    for book in book_list:
        if book.title == book_to_find:
            print(f"Book {book.title} found")
            return book
    print(f"Sorry, no book was found called {book_to_find}")
    return None


def lend_book():
    user = find_user()
    print()
    if user:  # only if the user is found
        book = find_book()  # if the book is found
        if book.available:  # and book is available
            confirm = input(f"Type Y to confirm borrowing book {book.title}: ").upper()
            if confirm == "Y":
                print(f"Book title: {book.title} is now issued to user: {user.name}")
                book.available = False
                book.borrower = user.name
                user.borrowed.append(book.title)
        else:
            print(f"Sorry, book {book.title} is unavailable")


def return_book():
    user = find_user()
    print()
    if user:  # only if the user is found
        book = find_book()  # if the book is found
        if book.title in user.borrowed:
            confirm = input(f"Type Y to confirm returning book {book.title}: ").upper()
            if confirm == "Y":
                print(f"Book title: {book.title} is now returned to the library")
                book.available = True
                book.borrower = user.name
                user.borrowed.remove(book.title)
        else:
            print(f"Sorry, book {book.title} is on loan to someone else")


# MAIN ROUTINE
book_list = []
user_list = []
# Create books
Books("Lord of the Rings", "J.R.R.Tolkien", "TOL", "9780261103252")
Books("The Hunger Games", "Suzanne Collins", "COL", "9781407132082")
Books("A Tale of Two Cities", "Charles Dickens", "DIC", "9781853262647")
Books("Harry Potter", "J.K.Rowling", "ROW", "9780439321624")

# Create users
Users("John", "12 Example St")
Users("Susan", "1011 Binary Rd")
Users("Paul", "25 Appletree Dr")
Users("Mary", "8 Moon Cres")

# lend_book()
# print("\n#######################\n")
# return_book()
# find_user()
# find_book()
# add_book()
# print_info()
# add_user()
# print_user_info()

# User Menu
new_action = True
while new_action:
    print("1) Lend a book\n"
          "2) Return a book\n"
          "3) Add a user\n"
          "4) Add a book\n"
          "5) Exit\n")

    choice = input("\nWhat would you like to do - Enter number: ")
    if choice == "1":
        lend_book()
    elif choice == "2":
        return_book()
    elif choice == "3":
        add_user()
    elif choice == "4":
        add_book()
    elif choice == "5":
        print("Goodbye")
        new_action = False
    else:
        print("\nThat was not a valid input\n")