class Books:
    def __init__(self, title, author, dewy, isbn):
        self.title = title.title()
        self.author = author
        self.dewy = dewy
        self.isbn = isbn
        self.available = True
        self.borrower = None


# MAIN ROUTINE
books_list = []
