# Create a function that counts the number of digits in a number.
# Conversion of the number to a string is not allowed.
#
# Examples
# digits_count(4666) ➞ 4
#
# digits_count(544) ➞ 3
#
# digits_count(121317) ➞ 6
#
# digits_count(0) ➞ 1
#
# digits_count(12345) ➞ 5
#
# digits_count(1289396387328) ➞ 13
# Notes
# All inputs are integers but some are in exponential form, deal with it accordingly.

def digits_count(num):
    count = 0
    if num >= 0 and num <= 9: # here i'm checking whether its single digit and returning length as 1
        print(1)
    else:
        while num > 0:
            result = int(num) / 10
            count = count + 1
            num = result
        print(count - 1)


if __name__ == "__main__":
    digits_count(4666)  # 4
    digits_count(544)  # 3
    digits_count(121317)  # ➞ 6
    digits_count(0)  # ➞ 1
    digits_count(12345)  # ➞ 5
    digits_count(1289396387328)  # ➞ 13
