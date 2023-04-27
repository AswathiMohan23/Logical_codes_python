# Given a list of integers representing the color of each sock, determine how many pairs
# of socks with matching colors there are. For example, there are 7 socks with
# colors [1, 2, 1, 2, 1, 3, 2]. There is one pair of color 1 and one of color 2.
# There are three odd socks left, one of each color. The number of pairs is 2.
#
# Create a function that returns an integer representing the number of matching pairs of socks
# that are available.
#
# Examples
# sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]) ➞ 3
#
# sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]) ➞ 4
#
# sock_merchant([]) ➞ 0


def sock_merchant(num_list):
    value = num_list
    num_dict = {}
    count = 0
    for i in range(0, len(num_list)):
        for j in range(0, len(value)):
            if num_list[i] == value[j]:
                count = count + 1
        num_dict.update({num_list[i]: count})
        count = 0
    even = 0
    for i in num_dict:
        result = num_dict.get(i)
        if result % 2 == 0:
            pair = result / 2
            even = even + pair
        elif result == 1:
            pass
        else:
            pair = (result - 1) / 2
            if pair != 0:
                even = even + pair
    print("pairs of socks : ", int(even))


if __name__ == "__main__":
    sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20])  # ➞ 3
    sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90])  # ➞ 4
    sock_merchant([])  # ➞ 0
