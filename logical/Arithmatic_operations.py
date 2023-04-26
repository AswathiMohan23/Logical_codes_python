# Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").
#
# Here, we have 1 followed by a space, operator followed by another space and 2.
# For the challenge, we are going to have only two numbers between 1 valid operator. The return value
# should be a number.
#
# eval() is not allowed. In case of division, whenever the second number equals "0" return -1.
#
# For example:
#
# "15 // 0"  ➞ -1
# Examples
# arithmetic_operation("12 + 12") ➞ 24 // 12 + 12 = 24
#
# arithmetic_operation("12 - 12") ➞ 24 // 12 - 12 = 0
#
# arithmetic_operation("12 * 12") ➞ 144 // 12 * 12 = 144
#
# arithmetic_operation("12 // 0") ➞ -1 // 12 / 0 = -1


def arithmetic_operation(input_nums):
    input_nums.split('+')
    nums=""
    value=[]
    input_nums="".join(input_nums)
    for i in range(0,2):
        nums=nums+input_nums[i]
    value.append(nums)
    nums=""
    for i in range(5,7):
        nums = nums + input_nums[i]
    value.append(nums)
    operator=input_nums[3]
    first=int(str(value[0]))
    second = int(str(value[1]))
    if second == 0:
        return -1
    elif operator == '+':
        return first+second

    elif operator == '-':
        return second - first
    elif operator == '*':
        return first * second
    elif operator == '//':
        return first/second


if __name__=="__main__":
    print(arithmetic_operation("12 + 12")) # 24
    print(arithmetic_operation("12 - 12")) # 0
    print(arithmetic_operation("12 * 12")) # ➞ 144
    print(arithmetic_operation("12 // 0"))# ➞ -1 .......... 12 / 0 = -1)

