# Given a list of 10 numbers, return whether or not the list is shuffled sufficiently enough.
# In this case, if 3 or more numbers appear consecutively (ascending or descending), return False.
#
# Examples

# is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]) ➞ False
# # 9, 8, 7, 6 appear consecutively
#
# is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]) ➞ True
# # No consecutive numbers appear
# is_shuffled_well([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) ➞ True
# # No consecutive numbers appear
# Notes
# Only steps of 1 in either direction count as consecutive
# (i.e. a sequence of odd and even numbers would count as being properly shuffled (see example #4)).
# You will get numbers from 1-10.


def is_shuffled_well(num_list):
    output = []
    length = len(num_list)
    for i in num_list:
        if i + 1 == length or i + 1 > length or i + 2 == length or i + 2 == length:
            break
        else:
            if num_list[i] + 1 == num_list[i + 1] and num_list[i + 1] + 1 == num_list[i + 2]:
                output.append("yes")
            elif num_list[i] - 1 == num_list[i + 1] and num_list[i + 1] - 1 == num_list[i + 2]:
                output.append("yes")
            else:
                output.append("no")
    print(output)

    if 'yes' in output:
        return False
    else:
        return True


if __name__ == "__main__":
    print(is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]))  # ➞ False
    print(is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]))  # ➞ True
    print(is_shuffled_well([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]))  # ➞ True
