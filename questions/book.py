# Create a class called "Book" with attributes title, author, and year.
# Implement a method to display the
# book's details.
class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year

    def display(self):
        output= [self.__title, self.__author, self.__year]
        return output


if __name__=="__main__":
    obj=Book("abc","Tom",2010)
    print(obj.display())
