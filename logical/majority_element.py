# Given an array nums of size n, return the majority element. The majority element is the element that
# appears more than ⌊n / 2⌋ times.You may assume that the majority element always exists in the array.
#
# Example 1:
# Input: nums = [3, 2, 3]
# Output: 3
#
# Example 2:
# Input: nums = [2, 2, 1, 1, 1, 2, 2]
# Output: 2

def find_majority_element(num_list):
    length = len(num_list)
    max_count = 0
    index = 0
    for i in range(length):
        count = 1
        for j in range(i + 1, length):  # here we compare the element in ith position with i+1th position
            if num_list[i] == num_list[j]:
                count = count + 1
        if count > max_count:  # update maxCount if count of current element is greater
            max_count = count
            index = i
    if max_count > length // 2:  # if maxCount is greater than length/2 return the corresponding element
        print(num_list[index])
    else:
        print("No Majority Element")


if __name__ == "__main__":
    num_list = [2, 2, 1, 1, 1, 2, 2]
    find_majority_element(num_list)
