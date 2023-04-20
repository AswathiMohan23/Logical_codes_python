# Given a signed 32 - bit integer x, return x with its digits reversed.If reversing x causes
# the value to go outside the signed 32-bit integer range[-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64 - bit integers(signed or unsigned).
#
# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321


def reverse_func(input_number):
    num = input_number
    reverse = 0
    if input_number < 0:
        input_number = input_number * -1
    while input_number != 0:
        reminder = input_number % 10
        reverse = reverse * 10 + reminder
        input_number = input_number // 10
    if num < 0:
        reverse = -1 * reverse
        print("reverse no is : ", reverse)
    else:
        print("reverse no is : ", reverse)


if __name__ == '__main__':
    input_number = -657
    reverse_func(input_number)

    # 123%10 =3
    # quo =12/10 =1,
    # quo=12/10=quo=1,rem=2
