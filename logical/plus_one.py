# You are given a large integer represented as an integer array digits, where each digits[i] is the
# ith digit of the integer.The digits are ordered from most significant  to least significant in
# left - to - right order.The large integer does not contain any leading 0 's.
# Increment the large integer by one and return the resulting array of digits.

# Example 1:
# Input: digits = [1, 2, 3]
# Output: [1, 2, 4]

# Explanation: The array represents the integer 123. Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be[1, 2, 4].

def solution(digits):
    result = []
    for i in range(1, len(digits) + 1):
        if i == len(digits):
            i = i + 1
        result.append(i)
    # output = list(map(str, result))
    # output = ''.join(output)
    print(result)


if __name__ == "__main__":
    digits = [1, 2, 3]
    solution(digits)
