# Create a function that takes two number strings and returns their sum as a string.
#
# Examples
# add("111", "111") ➞ "222"
#
# add("10", "80") ➞ "90"
#
# add("", "20") ➞ "Invalid Operation"

def solution(input_list):
    sum=0
    for i in input_list:
        if i == " " or i == "":
            print("Invalid operation. Provide valid elements")
            break
        else:
            sum=sum+int(i)
            print(str(sum))


if __name__ == "__main__":
    input_list = [" ","111"]
    solution(input_list)