# Create a function that takes a list of numbers lst, a string s and return a list of numbers
# as per the following rules:
#
# "Asc" returns a sorted list in ascending order.
# "Des" returns a sorted list in descending order.
# "None" returns a list without any modification.
# Examples
# asc_des_none([4, 3, 2, 1], "Asc" ) ➞ [1, 2, 3, 4]
#
# asc_des_none([7, 8, 11, 66], "Des") ➞ [66, 11, 8, 7]
#
# asc_des_none([1, 2, 3, 4], "None") ➞ [1, 2, 3, 4]


def ascending(input_list, length_of_list):
    for i in range(length_of_list):
        for j in range(0, length_of_list - i - 1):
            if input_list[j] > input_list[j + 1]:
                (input_list[j+1], input_list[j]) = (input_list[j], input_list[j+1])


def descending(input_list, length_of_list):
    for i in range(length_of_list):
        for j in range(0, length_of_list - i - 1):
            if input_list[j] < input_list[j + 1]:
                (input_list[j], input_list[j + 1]) = (input_list[j + 1], input_list[j])


def solution(input_list, input_string):
    length_of_list = len(input_list)
    input_string = input_string.upper()
    if input_string == "ASC":
        ascending(input_list, length_of_list)
    elif input_string == "DEC":
        descending(input_list, length_of_list)


if __name__ == "__main__":
    input_list = [1, 3, 2, 6]
    print("input list : ",input_list)
    input_string = "Dec"
    solution(input_list, input_string)
    print(input_list)
