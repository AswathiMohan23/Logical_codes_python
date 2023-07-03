# Given an unsorted integer array, find all triplets in it with sum less than or equal
# to a given number.
#
# Input : nums[] = [2, 7, 4, 9, 5, 1, 3], target = 10
# Output: {(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 2, 7), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5)}
#
# Input : nums[] = [3, 5, 7, 3, 2, 1], target = 5
# Output: {}
#
# Since the input can have multiple triplets with sum less than or equal to the target,
# the solution should return a set containing all the distinct triplets in any order.
#
# '''

def triplets(input_list, target):
    sorted_list = []
    output = []
    for i in range(len(input_list)):
        sorted_list.clear()
        for j in range(len(input_list)):
            for k in range(len(input_list)):
                if input_list[i] != input_list[j] and input_list[j] != input_list[k] and input_list[k] != input_list[i]:
                    if input_list[i] + input_list[j] + input_list[k] <= target:
                        value = [input_list[i], input_list[j], input_list[k]]
                        sorted_list = sorted(value)
                        if sorted_list not in output:
                            output.append(sorted_list)
    print(output)


if __name__ == "__main__":
    triplets([2, 7, 4, 9, 5, 1, 3], 10)
    # Output: {(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 2, 7), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5)}

    triplets([3, 5, 7, 3, 2, 1], 5)  # Output: {}
