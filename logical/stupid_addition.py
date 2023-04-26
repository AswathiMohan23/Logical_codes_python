# Create a function that takes two parameters and, if both parameters are strings,
# add them as if they were integers or if the two parameters are integers, concatenate them.
#
# Examples
# stupid_addition(1, 2) ➞ "12"
#
# stupid_addition("1", "2") ➞ 3
#
# stupid_addition("1", 2) ➞ None

def stupid_addition(value1, value2):
    if isinstance(value1,int) and isinstance(value2,int):
        return str(value1) + str(value2)
    elif isinstance(value1,str) and isinstance(value2,str):
        return int(value1) + int(value2)
    else:
        return None


if __name__ == "__main__":
    print(stupid_addition(1, 2))  # ➞ "12"
    print(stupid_addition("1", "2"))  # ➞ 3
    print(stupid_addition("1", 2))  # none
