# Write a function that takes coordinates of two points on a two-dimensional plane
# and returns the length of the line segment connecting those two points.
#
# Examples
# line_length([15, 7], [22, 11]) ➞ 8.06
#
# line_length([0, 0], [0, 0]) ➞ 0
#
# line_length([0, 0], [1, 1]) ➞ 1.41
import math


def line_length(line1, line2):
    value=math.sqrt(math.pow((line2[0]-line1[0]),2)+math.pow((line2[1]-line1[1]),2))
    return round(value,2) # to round value up to 2 decimal points


if __name__ == "__main__":
    print(line_length([15, 7], [22, 11]))  # ➞ 8.06
    print(line_length([0, 0], [0, 0])) # ➞ 0
    print(line_length([0, 0], [1, 1])) # ➞ 1.41