# Write a function that adds two numbers. The catch, however, is that the numbers will be strings.
#
# Examples
# add_str_nums("4", "5") ➞ "9"
#
# add_str_nums("abcdefg", "3") ➞ "-1"
#
# add_str_nums("1", "") ➞ "1"
#
# add_str_nums("1874682736267235927359283579235789257", "32652983572985729") ➞ "1874682736267235927391936562808774986"
# Notes
# If there are any non-numerical characters, return "-1".
# An empty parameter should be treated as "0".
# Your function doesn't have to add negative numbers.
# Zeros at the beginning of the string should be trimmed.

def add_str_nums(first, second):
    if first.isalpha() and isinstance(int(second), int):
        print(-1)
    elif isinstance(int(first), int) and second == "":
        print(1)
    elif isinstance(first, str) and isinstance(second, str):
        print(int(first) + int(second))


if __name__ == "__main__":
    add_str_nums("4", "5")  # ➞ "9"
    add_str_nums("abcdefg", "3")  # ➞ "-1"
    add_str_nums("1", "")  # ➞ "1"
    add_str_nums("1874682736267235927359283579235789257", "32652983572985729")
    # ➞ "1874682736267235927391936562808774986"
