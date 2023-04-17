# Given an integer n,return a string array answer(1 - indexed)
# where: answer[i] == "FizzBuzz" if i is divisible by 3 and 5. answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5. answer[i] == i( as a string) if none of the above conditions are true.
# Example 1: Input: n = 3
# Output: ["1", "2", "Fizz"]

# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]

# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]


class Solution:
    output = []

    def func(self, number):
        for i in range(1, number + 1):
            if i % 3 == 0 and i % 5 == 0:
                self.output.append("FizzBuzz")
            elif i % 3 == 0 and i % 5 != 0:
                self.output.append("Fizz")
            elif i % 5 == 0 and i % 3 != 0:
                self.output.append("Buzz")

            else:
                self.output.append(i)
        print(self.output)


if __name__ == "__main__":
    number = 15
    obj = Solution()
    obj.func(number)
