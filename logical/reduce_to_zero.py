# Given an integer num, return the number of steps to reduce it to zero. In one step,
# if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
# Example 1: Input: num = 14
# Output: 6

# Explanation: Step 1) 14 is even; divide by 2 and obtain 7.
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3.
# Step 4) 3 is odd; subtract 1 and obtain 2.
# Step 5) 2 is even; divide by 2 and obtain 1.
# Step 6) 1 is odd; subtract 1 and obtain 0.

# Example 2) : Input: num = 123 ,       Example 3) :Input: num = 8
#               Output: 12                              Output: 4

class Solution:
    def solution(self, number, count):
        if number % 2 == 0:
            number = number / 2
            count = count + 1
        elif number % 2 != 0:
            number = number - 1
            count = count + 1
        if number != 0:
            self.solution(number, count)
        elif number == 0:
            print(count)


if __name__ == "__main__":
    number = 14
    count = 0
    obj = Solution()
    obj.solution(number, count)
