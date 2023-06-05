# Create a function that takes a list and string. The function should remove the letters
# in the string from the list, and return the list.
#
# Examples
# remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]
#
# remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]
#
# remove_letters(["d", "b", "t", "e", "a", "i"], "questions_from_edabit") ➞ []
# Notes
# If number of times a letter appears in the list is greater than the number of times the letter appears
# in the string, the extra letters should be left behind (see example #2).
# If all the letters in the list are used in the string, the function should return an empty
# list (see example #3).

def removing_letters(string_input, list_input):
    output_list = []
    string_to_list = list(string_input)
    [string_to_list.remove(i) if i in string_to_list else output_list.append(i) for i in list_input] # ternary operation here if acts like' ?' and else as ':'
    print("output : ", output_list)


if __name__ == "__main__":
    string_input = "string"
    list_input = ["s", "t", "r", "i", "n", "g", "g", "w"]
    print("input string : ", string_input)
    print("input list : ", list_input)
    removing_letters(string_input, list_input)
