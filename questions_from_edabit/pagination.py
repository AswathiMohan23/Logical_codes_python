# Pagination Class with OOP
# Your task is to create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.
#
# Example
#
# The pagination class will accept 2 parameters:
#
# items (default: []): A list of contents to paginate.
#
# pageSize (default: 10): The amount of items to show in each page.
#
# So for example we could initialize our pagination like this:
#
# alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')
#
# p = Pagination(alphabetList, 4)
# And then use the method getVisibleItems to show the contents of the paginated list.
#
# p.getVisibleItems() # ["a", "b", "c", "d"]
# You will have to implement various methods to go through the pages such as:
#
# prevPage
# nextPage
# firstPage
# lastPage
# goToPage
# Here's a continuation of the example above using nextPage and lastPage:
#
# p.nextPage()
#
# p.getVisibleItems()
# # ["e", "f", "g", "h"]
#
# p.lastPage()
#
# p.getVisibleItems()
# # ["y", "z"]
# Notes
# The second argument (pageSize) could be a float, in that case just convert it to
# an int (this is also the case for the goToPage method) The methods used to change page should be
# chainable, so you can call them one after the other like this: p.nextPage().nextPage()
# Please set the p.totalPages and p.currentPage attributes to the appropriate number as there
# cannot be a page 0. If a page is outside of the totalPages attribute, then the goToPage method
# should go to the closest page to the number provided (e.g. there are only 5 total pages, but
# p.goToPage(10) is given: the p.currentPage should be set to 5; if 0 or a negative number is given,
# p.currentPage should be set to 1).

class Pagination:
    def __init__(self, alphabet_list, page_size):
        self.items = alphabet_list
        self.page_size = page_size
        self.nextPage = 0
        self.input_list = []
        self.previous_page = []
        self.count = 0
        self.currentPage=0

    def getVisibleItems(self):
        new_list = list(self.items)
        result = []
        [self.input_list.extend(list(i)) for i in new_list]
        for i in range(0, self.page_size):
            self.count += 1
            result.append(self.input_list[i])
        self.previous_page.insert(0,result)
        return self.previous_page


    def get_nextPage(self):
        self.currentPage+=1
        next_page = []
        next = self.page_size + self.count
        for i in range(self.count, next):
            self.count += 1
            next_page.append(self.input_list[i])
        self.previous_page.extend([next_page])

        return next_page

    def get_previousItems(self):
        return self.previous_page[self.currentPage]

    def get_firstPage(self):
        return self.previous_page[0]

    def get_lastPage(self):
        return self.previous_page[len(self.previous_page) - 1]

    def get_goToPage(self, num):
        return self.previous_page[num - 1]


if __name__ == "__main__":
    alphabetList = "abcdefghijklmnopqrstuvwxyz".split('  ')
    #
    obj = Pagination(alphabetList, 5)
    print(obj.getVisibleItems()) #first 5
    print(obj.get_nextPage()) #next 5
    print(obj.get_nextPage()) #again next 5
    print(obj.get_previousItems()) #previous 5
    print(obj.get_firstPage())  #first 5
    print(obj.get_lastPage()) #last 5
    print(obj.get_goToPage(2)) #go to specified page
