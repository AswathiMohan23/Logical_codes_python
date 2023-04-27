# Create a class with a few functions like these examples.
#
# magic.replace("string", 'char', char') is a function that replaces all of the
# specified characters with different specified characters.
# magic.str_length("string") is a function that returns the length of the string.
# magic.trim(" string ") is a function that returns a string with truncated spaces at both
# the beginning and end.
# magic.list_slice(list, tuple) is a function that returns the items in the list that
# are between the specified indexes. If the length of the new list is 0, return -1.
# Examples
# magic.replace("AzErty-QwErty", "E", "e") ➞ "Azerty-Qwerty"
#
# magic.str_length("hello world") ➞ 11
#
# magic.trim("      python is awesome      ") ➞ "python is awesome"
#
# magic.list_slice([1, 2, 3, 4, 5], (2, 4)) ➞ [ 2, 3, 4 ]


def replace(first, second, third):
    output = []
    first = list(first)
    for i in range(0, len(first)):
        if first[i] == second:
            first[i] = third
        output.append(first[i])
    output = "".join(output)
    print(output)


def str_length(sentence):
    sentence = list(sentence)
    print(len(sentence))


def trim(sentence):
    print(sentence.strip())  # strip used to delete blank space from begining


def list_slice(input_list, index):
    output = [index[0]]
    for i in range(0, len(input_list)):
        if index[0] <= i < index[1]:
            output.append(input_list[i])
    print(output)


if __name__ == "__main__":
    replace("AzErty-QwErty", "E", "e")  # ➞ "Azerty-Qwerty"
    str_length("hello world")  # ➞ 11
    trim("      python is awesome      ")  # ➞ "python is awesome"
    list_slice([1, 2, 3, 4, 5], (2, 4))  # ➞ [2, 3, 4]
