# Create a function that takes a number as an argument, increments the number by +1 and
# returns the result.
#
# Examples
# addition(0) ➞ 1
#
# addition(9) ➞ 10
#
# addition(-3) ➞ -2

def solution(num):
    if num < 0:
        num = num - 1  # if num=-3 then num-1 =-3-1 ie, -4
    else:
        num = num + 1
    return num


if __name__ == "__main__":
    num = -3
    output = solution(num)
    print("output is : ", output)
