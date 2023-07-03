# Given an integer array, find the maximum difference between two elements in it
# such that the smaller element appears before the larger element. If no such pair exists,
# return any negative number.
#
# Input : [2, 7, 9, 5, 1, 3, 5]
# Output: 7
# Explanation: The pair with the maximum difference is (2, 9).
#
# Input : [5, 4, 3, 2, 1]
# Output: -1 (or any other negative number)
# Explanation: No pair with the maximum difference exists.

def sorting(output):
    for i in range(len(output)):
        for j in range(0, len(output) - i - 1):
            if output[j] < output[j + 1]:
                output[j + 1], output[j] = output[j], output[j + 1]
    return output


def finding_pair(input_list):
    output = []
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if input_list[i] < input_list[j]:
                diff = input_list[j] - input_list[i]
            else:
                diff = input_list[j] - input_list[i]
            output.append(diff)
    output = sorting(output)
    return output[0]


if __name__ == "__main__":
    print(finding_pair([2, 7, 9, 5, 1, 3, 5]))  # 7
    print(finding_pair([5, 4, 3, 2, 1]))  # -1
  