# Create a function that takes two number strings and returns their sum as a string.
#
# Examples
# add("111", "111") ➞ "222"
#
# add("10", "80") ➞ "90"
#
# add("", "20") ➞ "Invalid Operation"


def add(first, second):
    if first==" " or second== " ":
        print("invalid operation")
    else:
        sum= int(first)+int(second)
        print(sum)


if __name__ =="__main__":
    add("111", "111") # ➞ "222"
    add("10", "80") # ➞ "90"
    add(" ", "20")  #➞ "Invalid Operation"