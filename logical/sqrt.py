# Given a non - negative integer x, return the square root of x rounded down to the nearest integer.The
# returned integer should be non - negative as well.  You must not use a built - in exponent
# function or operator.  For example, do not use
# pow(x, 0.5) in c + + or x ** 0.5 in python.
#
# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
#
# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest
# integer, 2 is returned.

def solution(num):
    result =num**(1/2)

    print(result//1)


if  __name__ == "__main__":
    num=8
    solution(num)