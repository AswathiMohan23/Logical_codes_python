# 2. Create a function that takes a list of numbers between 1 and 10 (excluding one number)
# and returns the missing number.
#
# Examples
# missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
# missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10
# missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7
# Notes
# The list of numbers will be unsorted (not in order).
# Only one number will be missing.


def find_missing_number(input_list, first_number, last_number):
    num_list = []
    [num_list.append(i) for i in range(first_number, last_number + 1)]
    [num_list.remove(i) for i in input_list for j in num_list if i == j]
    print(num_list)


def swap(input_list, j, param):
    temp = input_list[j + 1]
    input_list[j + 1] = input_list[j]
    input_list[j] = temp


def bubbleSort(input_list, length_of_list):
    [swap(input_list, j, j + 1) for j in range(length_of_list - 1) if input_list[j] > input_list[j + 1]]
    if length_of_list - 1 > 1:
        bubbleSort(input_list, length_of_list - 1)


if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 6, 8, 9, 10]
    bubbleSort(input_list, len(input_list))
    first_num = input_list[0]
    last_num = input_list[len(input_list) - 1]
    find_missing_number(input_list, first_num, last_num)
