# To the Right, to the Right!
# Create a class that imitates a select screen. For simplicity, the cursor can only move right!
#
# In the display method, return a string representation of the list, but with square brackets
# around the currently selected element. Also, create the method to_the_right, which moves the
# cursor one element to the right.
#
# The cursor should start at index 0.
#
# Examples
# menu = Menu([1, 2, 3])
# menu.display() ➞ "[[1], 2, 3]"
# menu.to_the_right()
# menu.display() ➞ "[1, [2], 3]"
#
# menu.to_the_right()
# menu.display() ➞ "[1, 2, [3]]"
#
# menu.to_the_right()
# menu.display() ➞ "[[1], 2, 3]"

class Screen:

    def __init__(self, input_list):
        self.input_list = input_list
        self.count = 0
        self.output_list = []

    def to_right(self):
        self.output_list.clear()
        [self.output_list.append([self.input_list[i]]) if self.count == i else self.output_list.append(
            self.input_list[i])for i in range(0, len(self.input_list))]
        self.count = self.count + 1

    def display(self):
        return self.output_list


if __name__ == "__main__":
    menu = Screen([1, 2, 3])
    menu.to_right()
    print(menu.display()) #[[1], 2, 3]
    menu.to_right()
    print(menu.display()) #[1, [2], 3]
    menu.to_right()
    print(menu.display()) #[1, 2, [3]]
