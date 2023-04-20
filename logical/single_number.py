# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one. You must implement a solution with a linear runtime complexity and
# use only constant extra space.
# Example 1:
# Input: nums = [2, 2, 1]
# Output: 1

# Example 2:
# Input: nums = [4, 1, 2, 1, 2]
# Output: 4

def solution(nums):
    count = 0
    output = {}
    for i in nums:
        j = i + 1
        for j in nums:
            if i == j:
                count = count + 1
        output.update({i: count})
        count = 0
    print(output)
    min_key = min(output.values())
    result = [key for key in output if output[key] == min_key]
    print("the number which is not repeated is : ", result)


if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    solution(nums)
