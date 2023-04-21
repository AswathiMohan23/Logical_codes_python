# Create a function that takes a number num and returns its length.
#
# Examples
# number_length(10) ➞ 2
#
# number_length(5000) ➞ 4
#
# number_length(0) ➞ 1
# Notes
# The use of the len() function is prohibited.

def solution(num):
    num = str(num)
    num = list(num)
    count = 0
    for _ in num: # not using variable so instead can give _
        count += 1
    print("the length is : ", count)


if __name__ == "__main__":
    num = 5000
    solution(num)
