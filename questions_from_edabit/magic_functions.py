# Create a class with a few functions like these examples.
#
# magic.replace("string", 'char', char') is a function that replaces all of the specified
# characters with different specified characters.
# magic.str_length("string") is a function that returns the length of the string.
# magic.trim(" string ") is a function that returns a string with truncated spaces at both the beginning
# and end.magic.list_slice(list, tuple) is a function that returns the items in the list that are
# between the specified indexes. If the length of the new list is 0, return -1.
# Examples
# magic.replace("AzErty-QwErty", "E", "e") ➞ "Azerty-Qwerty"
#
# magic.str_length("hello world") ➞ 11
#
# magic.trim("      python is awesome      ") ➞ "python is awesome"
#
# magic.list_slice([1, 2, 3, 4, 5], (2, 4)) ➞ [ 2, 3, 4 ]

class Magic:

    def replace(self, word, char1, char2):
        result=""
        for i in word:
            if i.isalpha() and i==char1:
                result=result+char2
            elif i.isalpha():
                result=result+i
        return result

    def str_length(self, input):
        return len(input)

    def trim(self, sentence):
        return sentence.strip()

    def list_slice(self, param, param1):
        result=[]
        end=param1[1]
        for i in range(param1[0],end+1):
            result.append(i)
        return result
        # return param[1:4]


if __name__=="__main__":
    magic=Magic()
    print(magic.replace("AzErty-QwErty", "E", "e"))
    print(magic.str_length("hello world")) #➞ 11
    print(magic.trim("      python is awesome      ")) #➞ "python is awesome"
    print(magic.list_slice([1, 2, 3, 4, 5], (2, 4))) #➞ [ 2, 3, 4 ])