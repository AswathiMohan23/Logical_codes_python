# Write a function that accepts the height and width (m, n) and an optional proc s and generates a list with m elements. Each element is a string consisting of either:
#
# The default character (hash #) repeating n times (if no proc is given).
# The character passed in through the proc repeating n times.
# Examples
# make_rug(3, 5, '#') ➞ [
#   "#####",
#   "#####",
#   "#####"
# ]
#
# make_rug(3, 5, '$')  ➞ [
#   "$$$$$",
#   "$$$$$",
#   "$$$$$"
# ]
#
# make_rug(2, 2, 'A')  ➞ [
#   "AA",
#   "AA"
# ]


def make_rug(breadth, length, symbol):
    for i in range(0,breadth):
        for j in range(0,length):
            print(symbol,end=" ")
        print("\n")


if __name__=="__main__":
    make_rug(3, 5, '#') #➞ [
    #   "#####",
    #   "#####",
    #   "#####"
    # ]
    make_rug(3, 5, '$')  #➞ [
    #   "$$$$$",
    #   "$$$$$",
    #   "$$$$$"
    # ]

    make_rug(2, 2, 'A') # ➞ [
    #   "AA",
    #   "AA"
    # ]
