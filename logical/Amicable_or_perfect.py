# Given a positive number x, if all the positive divisors of x (excluding x) add up to x,
# then x is said to be a perfect number.
#
# For example, the set of positive divisors of 6 excluding 6 itself is (1, 2, 3).
# The sum of this set is 6. Therefore, 6 is a perfect number.
#
# Given a positive number x, if all the positive divisors of x add up to a second number y,
# and all the positive divisors of y add up to x, then x and y are said to be a pair of amicable numbers.
#
# Create a function that takes a number and returns "Perfect" if the number is perfect,
# "Amicable" if the number is part of an amicable pair, or "Neither".
#
# Examples
# num_type(6) ➞ "Perfect"
#
# num_type(2924) ➞ "Amicable"
#
# num_type(5010) ➞ "Neither"


def solution(num):
    factors = []
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)
            sum = sum + i
        else:
            pass
    return sum


def num_type(num):
    sum1 = solution(num)
    if sum1 == num:
        return "perfect"
    sum2 = solution(sum1)
    return "Amicable" if sum2 == num else "Neither"


if __name__ == "__main__":
    print(num_type(6))  # ➞ "Perfect"
    print(num_type(2924))  # ➞ "Amicable"
    print(num_type(5010))  # ➞ "Neither"
