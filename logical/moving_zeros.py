# Given an integer array nums, move all 0 's to the end of it while maintaining the relative order' \
# of the non-zero elements. Note that you must do this in -place without making a copy of the array.

# Example 1:
# Input: nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
#
# Example2:
# Input: nums = [0]
# Output: [0]


def moving_zeros(input_nums):
    zero_list=[]
    output_list=[]
    [zero_list.append(i) if i == 0 else output_list.append(i) for i in input_nums]
    # ternary operation here if acts like' ?' and else as ':'
    output_list.extend(zero_list)
    print("After moving zeros to the end, the resultant list is : ",output_list)


if __name__ == "__main__":
    input_list = [0, 1, 0, 3, 12]
    print(input_list)
    moving_zeros(input_list)

