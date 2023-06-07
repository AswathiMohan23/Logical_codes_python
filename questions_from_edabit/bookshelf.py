# Create a Book class that has two attributes:
#
# .title
# .author
# and two methods:
#
# A method named .get_title() that returns: "Title: " + the instance title.
# A method named .get_author() that returns: "Author: " + the instance author.
# and instantiate this class by creating 3 new books:
#
# Pride and Prejudice - Jane Austen (PP)
# Hamlet - William Shakespeare (H)
# War and Peace - Leo Tolstoy (WP)
# The name of the new instances should be PP, H, and WP, respectively.
#
# For instance, if I instantiated the following book using this Book class:
#
# Harry Potter - J.K. Rowling (HP)
# I would get the following attributes and methods:
#
# Examples
# HP.title ➞ "Harry Potter"
# HP.author ➞ "J.K. Rowling"
# HP.get_title() ➞ "Title: Harry Potter"
# HP.get_author() ➞ "Author: J.K. Rowling"

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def get_title(self):
        return f'Title : {self.title}'

    def get_author(self):
        return f'Author : {self.author}'


if __name__=="__main__":
    pp=Book("Pride and Prejudice","Jane Austen")
    h=Book("Hamlet","William Shakespeare")
    wp=Book("War and Peace","Leo Tolstoy")
    print(pp.get_title())
    print(pp.get_author())
    print(h.get_title())
    print(h.get_author())
    print(wp.get_title())
    print(wp.get_author())
