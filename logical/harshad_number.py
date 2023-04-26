# A number is said to be Harshad if it 's exactly divisible by the sum of its digits.
# Create a function that determines whether a number is a Harshad or not.
#
# Examples
# is_harshad(75) ➞ False
# # 7 + 5 = 12
# # 75 is not exactly divisible by 12
#
# is_harshad(171) ➞ True
# # 1 + 7 + 1 = 9
# # 9 exactly divides 171
#
# is_harshad(481) ➞ True
#
# is_harshad(89) ➞ False
#
# is_harshad(516) ➞ True
#
# is_harshad(200) ➞ True


def is_harshad(number):
    input_nuumber=number
    number=list(str(number))
    sum=0
    for i in number:
        sum=sum+int(i)
    return True if input_nuumber%sum == 0 else False


if __name__ == "__main__":
   print(is_harshad(75))     # ➞ False
   print(is_harshad(171))    # ➞ True
   print(is_harshad(481)) # ➞ True
   print(is_harshad(89)) # ➞ False
   print(is_harshad(516)) # ➞ True
   print(is_harshad(200)) # ➞ True
