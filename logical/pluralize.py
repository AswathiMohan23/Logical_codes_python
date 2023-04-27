# Given a list of words in the singular form, return a set of those words in the plural form
# if they appear more than once in the list.
#
# Examples
# pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }
#
# pluralize(["table", "table", "table"]) ➞ { "tables" }
#
# pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }
# Notes
# This is an oversimplification of the English language so no edge cases will appear.
# Only focus on whether or not to add an s to the ends of words.
# All tests will be valid.

def pluralize(input_list):
    output = []
    list_names=list(set(input_list)) # converted to set and then to list to avoid duplicate values
    if len(list_names)==len(input_list):
        print(set(input_list))
    else:
        for i in range(0, len(list_names)):
            count = 0
            for j in range(0, len(input_list)):
                if list_names[i] == input_list[j]:
                    count = count + 1

            if count > 1:
                plural = list_names[i] + 's'
                output.append(plural)
        print(set(output))


if __name__ == "__main__":
    pluralize(["cow", "pig", "cow", "cow"])  # ➞ {"cows", "pig"}
    pluralize(["table", "table", "table"])  # ➞ {"tables"}
    pluralize(["chair", "pencil", "arm"])  # ➞ { "chair", "pencil", "arm" }
