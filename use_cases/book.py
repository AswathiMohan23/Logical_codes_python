# Problem Statement:
#
# ## Implement a library management system with the following classes:
#
# ---
#
# 1.  Library class:
#
#     -   Attributes:
#
#         1. name (string)
#         2. books (list of Book objects)
#
#     -   Methods:
#         1. add_book(book): Add a new book to the library.
#         2. get_total_books(): Return the total number of books in the library.
#         3. get_available_books(): Return the number of available books.
#         4. get_borrowed_books(): Return the number of borrowed books.
#         5. get_books_by_author(author): Return a list of books written by a specific author.
#         6. get_books_by_genre(genre): Return a list of books in a specific genre.
#         7. borrow_book(book_id, borrower): Borrow a book from the library.
#         8. return_book(book_id): Return a borrowed book to the library.
#         9. get_book_details(book_id): Return the details of a specific book.
#
# 2.  Book class:
#
#     -   Attributes
#
#         1. book_id (integer)
#         2. title (string)
#         3. author (string)
#         4. genre (string)
#         5. borrowed (boolean)
#
#     -   Methods:
#         -   None
#
# ---
#
# #### Your task is to implement these classes and write a program to simulate the
# library management system. The program should allow the user to perform the following operations:
#
# -   [] Add books to the library.
# -   [] Retrieve and display the total number of books.
# -   [] Retrieve and display the number of available books.
# -   [] Retrieve and display the number of borrowed books.
# -   [] Retrieve and display a list of books written by a specific author.
# -   [] Retrieve and display a list of books in a specific genre.
# -   [] Borrow a book from the library.
# -   [] Return a borrowed book to the library.
# -   [] Retrieve and display the details of a specific book.
#
# **Note:** You are free to design the program structure and logic as per your understanding
# and preferences. The problem statement provides a basic outline of the required
# classes and their methods. You may add additional methods or attributes to enhance the
# functionality of the library management system.

class Book:
    def __init__(self, book_id, title, author, genre, borrowed=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.borrowed = borrowed



class Library:
    def __init__(self):
        self.name = ""
        self.books = {}

    def add_book(self, book:Book):
        self.books[book.book_id]=book
        return f"Book '{book.book_id,book.title,book.author,book.genre} has been added to the book list"

    def get_total_books(self):
        return f"total no of books :{len(self.books)}"

    def get_available_books(self):
        return f"total no of available books :{len([self.books for i in self.books.values() if not i.borrowed])}"

    def get_borrowed_books(self):
        return f"total no of borrowed books :{len([self.books for i in self.books.values() if  i.borrowed])}"


    def get_books_by_author(self,author):
        book_list=[]
        for i in self.books:
            value=self.books.get(i)
            book:Book=value
            if book.author==author:
                book_list.append(book.title)
        return f"by author {book_list}"



    def return_book(self, book_id):
        book:Book=self.books.get(book_id)
        book.borrowed=False
        return book.borrowed

    def get_book_details(self, book_id):
        book:Book=self.books.get(book_id)
        return {book.book_id,book.title,book.author,book.genre}

    def get_books_by_genre(self, genre):
        book_list = []
        for i in self.books:
            value = self.books.get(i)
            book: Book = value
            if book.genre == genre:
                book_list.append(book.title)
        return f"by genre {book_list}"

    def borrow_book(self, book_id, borrower):
        book:Book=self.books.get(book_id)
        book.borrowed=True
        return f"{book.borrowed} borrowed by {borrower}"


if __name__=="__main__":
    library=Library()
    book1=Book(book_id=1,title="abc",author="aaa",genre="novel")
    book2=Book(book_id=2,title="def",author="bbb",genre="sc-fi",borrowed=True)
    book3=Book(book_id=3,title="lmn",author="ccc",genre="short story",borrowed=True)
    book4=Book(book_id=4,title="xyz",author="aaa",genre="short story",borrowed=True)

# 1. add_book(book): Add a new book to the library.
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

# 2. get_total_books(): Return the total number of books in the library.
    print(library.get_total_books())

# 3. get_available_books(): Return the number of available books.
    print(library.get_available_books())

# 4. get_borrowed_books(): Return the number of borrowed books.
    print(library.get_borrowed_books())

# 5. get_books_by_author(author): Return a list of books written by a specific author.
    print(library.get_books_by_author("aaa"))
# 6. get_books_by_genre(genre): Return a list of books in a specific genre.
    print(library.get_books_by_genre("novel"))
# 7. borrow_book(book_id, borrower): Borrow a book from the library.
    print(library.borrow_book(1, "riya"))

# 8. return_book(book_id): Return a borrowed book to the library.
    print(library.return_book(2))
# 9. get_book_details(book_id): Return the details of a specific book.
    print(library.get_book_details(1))








