# A quadratic equation a x² + b x + c = 0 has either 0, 1, or 2 distinct solutions for real values of x. Given a, b and c, you should return the number of solutions to the equation.
#
# Examples
# solutions(1, 0, -1) ➞ 2
# // x² - 1 = 0 has two solutions (x = 1 and x = -1).
#
# solutions(1, 0, 0) ➞ 1
# // x² = 0 has one solution (x = 0).
#
# solutions(1, 0, 1) ➞ 0
# // x² + 1 = 0 has no real solutions.
import math


# Notes
# You do not have to calculate the solutions, just return how many there are.
# a will always be non-zero.


def solution(a, b, c):
    value=math.pow(b,2)-(4*a*c)
    if value > 0:
        return 2
    elif value == 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    # x² - 1 = 0===> a=1,b=-1,c=0
    a,b,c=1,0,0
    print(solution(a,b,c))
