# Write a function that takes a list of numbers and returns a list with two elements:
#
# The first element should be the sum of all even numbers in the list.
# The second element should be the sum of all odd numbers in the list.
# Example
# sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# # 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9
#
# sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])
#
# sum_odd_and_even([0, 0]) ➞ [0, 0])
# Notes
# Count 0 as an even number.


def solution(input_list):
    sum1 = 0
    sum2 = 0
    for i in input_list:
        if i % 2 == 0:
            sum1 = sum1 + i
        elif i % 2 != 0:
            sum2 = sum2 + i

    return sum1, sum2


if __name__ == "__main__":
    input_list = [-1, -2, -3, -4, -5, -6]
    print(solution(input_list))
