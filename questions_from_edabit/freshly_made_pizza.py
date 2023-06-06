# Create a Pizza class with the attributes order_number and ingredients (which is given as a list). Only the ingredients will be given as input.
#
# You should also make it so that its possible to choose a ready made pizza flavour rather than
# typing out the ingredients manually! As well as creating this Pizza class, hard-code the following
# pizza flavours.
#
# Name	Ingredients
# hawaiian	ham, pineapple
# meat_festival	beef, meatball, bacon
# garden_feast	spinach, olives, mushroom
# Examples
# p1 = Pizza(["bacon", "parmesan", "ham"])    # order 1
# p2 = Pizza.garden_feast()                  # order 2
# p1.ingredients ➞ ["bacon", "parmesan", "ham"]
#
# p2.ingredients ➞ ["spinach", "olives", "mushroom"]
#
# p1.order_number ➞ 1
#
# p2.order_number ➞ 2
# Notes
# All words are given in lowercase.
# See the Resources tab for some helpful tutorials on classes!

class Pizza:

    def __init__(self, ingredients=None, order_no=0):
        self.ingredients = ingredients
        self.order_no = order_no + 1


    def garden_feast(self):
        self.ingredients = ["spinach", "olives", "mushroom"]
        self.order_no += 1

    def meat_festival(self):
        self.ingredients = ['beef', 'meatball', 'bacon']
        self.order_no += 1

    def hawaiian(self):
        self.ingredients=['ham', 'pineapple']
        self.order_no+=1


if __name__ == "__main__":
    p1 = Pizza(["bacon", "parmesan", "ham"])  # order 1
    p2 = Pizza()
    p3 = Pizza()
    p4=Pizza()

    p2.garden_feast()
    print(p1.ingredients)  # ➞ ["bacon", "parmesan", "ham"]
    print(p1.order_no)  # ➞ 1
    #
    print(p2.ingredients)  # ➞ ["spinach", "olives", "mushroom"]
    print(p2.order_no)  # ➞ 2

