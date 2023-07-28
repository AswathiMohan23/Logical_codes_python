# Create a function that takes a list of numbers or strings and returns a list with
# the items from the original list stored into sublist. Items of the same value
# should be in the same sublist.
#
# Examples
# advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]
#
# advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]
#
# advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]
# Notes
# The sublist should be returned in the order of each element's first appearance in
# the given list.

def sorting(input_list, length):
    for i in range(length):
        for j in range(0, length - i - 1):
            if input_list[j] < input_list[j + 1]:
                (input_list[j], input_list[j + 1]) = (input_list[j], input_list[j + 1])
    return input_list


def advanced_sort(input_list):
    output = []
    visited_list = []
    sort_list = sorting(input_list, len(input_list))
    for i in range(len(sort_list)):
        if sort_list[i] not in visited_list:
            num = []
            for j in range(len(sort_list)):
                if sort_list[i] == sort_list[j]:
                    num.append(sort_list[i])
            visited_list.append(sort_list[i])
            output.append(num)
    return output


if __name__ == "__main__":
    print(advanced_sort([2, 1, 2, 1]))  # ➞ [[2, 2], [1, 1]]
    print(advanced_sort([5, 4, 5, 5, 4, 3]))  # ➞ [[5, 5, 5], [4, 4], [3]]
    print(advanced_sort(["b", "a", "b", "a", "c"]))  # ➞ [["b", "b"], ["a", "a"], ["c"]]

