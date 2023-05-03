# Given an integer array, find k'th smallest element in the array where k is a positive integer ' \
#                               'less than or equal to the length of array.
#
# Input : [7, 4, 6, 3, 9, 1], k = 3
# Output: 4
# Explanation: The 3rd smallest array element is 4
#
# Input : [1, 5, 2, 2, 2, 5, 5, 4], k = 5
# Output: 4
# Explanation: The 5th smallest array element is 4

def sort(value, length):
    for i in range(length):
        for j in range(0, length - i - 1):
            if value[j] > value[j + 1]:
                (value[j], value[j + 1]) = (value[j + 1], value[j])
    return value


def solution(input_list, num):
    length = len(input_list)
    sort(input_list, length)
    print(input_list)
    return input_list[num - 1]


if __name__ == "__main__":
    print(solution([1, 5, 2, 2, 2, 5, 5, 4], 6))  # 4
    print(solution( [7, 4, 6, 3, 9, 1],  3))  # 4
