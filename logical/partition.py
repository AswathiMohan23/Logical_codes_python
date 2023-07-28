# Write a function that returns True if you can partition a list into one element and the rest,
# such that this element is equal to the product of all other elements excluding itself.
#
# Examples
# can_partition([2, 8, 4, 1]) ➞ True
# # 8 = 2 x 4 x 1
#
# can_partition([-1, -10, 1, -2, 20]) ➞ False
#
# can_partition([-1, -20, 5, -1, -2, 2]) ➞ True
# Notes
# The list may contain duplicates.
# Multiple solutions can exist, any solution is sufficient to return True


def can_partition(input_list):
    product = 1
    output = []
    for i in range(len(input_list)):
        for j in range(len(input_list)):
            if i != j:
                product = product * input_list[j]
        if product == input_list[i]:
            output.append(True)
        else:
            output.append(False)
        product = 1
    return True if True in output else False


if __name__ == "__main__":
    print(can_partition([2, 8, 4, 1]))  # ➞ True
    print(can_partition([-1, -10, 1, -2, 20]))  # ➞ False
    print(can_partition([-1, -20, 5, -1, -2, 2]))  # ➞ True
