# Given an unsorted integer array, print all greater elements than all elements present to their right.
#
# Input : [10, 4, 6, 3, 5]
# Output: [10, 6, 5]
# Explanation: The elements that are greater than all elements to their right are 10, 6, and 5.
#
# Note: The solution should return the elements in the same order as they appear in the input array.


def solution(num):
    output = []
    length = len(num)
    for i in range(0, length - 1):
        if i == length:
            i = i - 1
            if num[i] > num[i + 1]:
                output.append(num[i])
                break
        else:
            if num[i] > num[i + 1]:
                output.append(num[i])
    output.append(num[length - 1])
    print(output)


if __name__ == "__main__":
    num = [10, 4, 6, 3, 5]
    solution(num)
