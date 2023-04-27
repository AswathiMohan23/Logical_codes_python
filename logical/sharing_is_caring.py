# Given a list of numbers, create a function that removes 25% from every number
# in the list except the smallest number, and adds the total amount removed to the smallest number.
#
# Examples
# show_the_love([4, 1, 4]) ➞ [3, 3, 3]
#
# show_the_love([16, 10, 8]) ➞ [14.5, 7.5, 12]
#
# show_the_love([2, 100]) ➞ [27, 75]

def show_the_love(num_list):
    output = []
    result = []
    input_list = num_list
    input_list.sort()
    smallest_num = input_list[0]
    for i in range(1, len(num_list)):
        value = num_list[i] * (25 / 100)
        remaining = num_list[i] - value
        smallest_num = smallest_num + value
        output.append(remaining)
    result.append(smallest_num)
    result.extend(output)
    print(result)


if __name__ == "__main__":
    show_the_love([4, 1, 4])  # ➞ [3, 3, 3]
    show_the_love([16, 10, 8])  # ➞ [14.5, 7.5, 12]
    show_the_love([2, 100])  # ➞ [27, 75]
