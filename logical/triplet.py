# Create a function that takes an unsorted list of numbers and returns the number
# of unique triplets whose sum is equal to the variable n.
#
# Examples
# triplet_sum([1, 0, 2, 6, 3, 9, 3], n = 11) ➞ 2
# # Since we found two unique triplets that equate to 11: 0+2+9 and 2+6+3
#
# triplet_sum([1, 2, 6, 3, 4, 5, 9, 10, 11], n = 20) ➞ 6
#
# triplet_sum([5, 2, 8], n = 2) ➞ 0
# Notes
# You should also expect lists with less than three elements.

def triplet_sum(input_list, num):
    result = []
    for i in range(0, len(input_list)):
        for j in range(i + 1, len(input_list)):
            for k in range(j, len(input_list)):
                if input_list[i] + input_list[j] + input_list[k] == num:
                    if str(str(f'{input_list[i]}+{input_list[j]}+{input_list[k]}')) not in result:
                        result.append(str(f'{input_list[i]}+{input_list[j]}+{input_list[k]}'))

    return len(result)


if __name__ == "__main__":
    print(triplet_sum([1, 0, 2, 6, 3, 9, 3], 11))  # ➞ 2
    print(triplet_sum([1, 2, 6, 3, 4, 5, 9, 10, 11], 20))  # ➞ 6
    print(triplet_sum([5, 2, 8], 2))  # ➞ 0)
