# Create a function that validates whether a number n is within the bounds of lower and upper.
# Return false if n is not an integer.
#
# Examples
# intWithinBounds(3, 1, 9) ➞ true
#
# intWithinBounds(6, 1, 6) ➞ false
#
# intWithinBounds(4.5, 3, 8) ➞ false
# Notes
# The term "within bounds" means a number is considered equal or greater than a lower bound
# and lesser (but not equal) to an upper bound, (see example #2).

# Bounds will be always given as integers.
def intWithinBounds(first, second, third):
    if isinstance(first, int) and isinstance(second, int) and isinstance(third, int):
        if first == third:
            return False
        elif second < first and second < third:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    print(intWithinBounds(3, 1, 9))  # true
    print(intWithinBounds(6, 1, 6))  # false
    print(intWithinBounds(4.5, 3, 8))  # false
