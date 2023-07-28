# When importing objects from a module in Python, the syntax usually is as follows:
#
# from module_name import object
# Given a string of an incorrect import statement, return the fixed string.
# All import statements will be the wrong way round.
#
# Examples
# fix_import("import object from module_name") ➞ "from module_name import object"
#
# fix_import("import randint from random") ➞ "from random import randint"
#
# fix_import("import pi from math") ➞ "from math import pi"

def fix_import(sentence):
    output = []
    sentence = sentence.split()
    output.append(sentence[2])
    output.append(sentence[3])
    output.append(sentence[0])
    output.append(sentence[1])
    output = " ".join(output)
    return output


if __name__ == "__main__":
    print(fix_import("import object from module_name"))  # ➞ "from module_name import object"
    print(fix_import("import randint from random"))  # ➞ "from random import randint"
    print(fix_import("import pi from math"))  # ➞ "from math import pi"
