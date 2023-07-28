# Create a function that, given a phrase and a number of letters guessed, returns
# a string with hyphens - for every letter of the phrase not guessed, and each letter guessed in place.
#
# Examples
# hangman("helicopter", ["o", "e", "s"]) ➞ "-e---o--e-"
#
# hangman("tree", ["r", "t", "e"]) ➞ "tree"
#
# hangman("Python rules", ["a", "n", "p", "r", "z"]) ➞ "P----n r----"
#
# hangman("He"s a very naughty boy!", ["e", "a", "y"]) ➞ "-e"- a -e-y -a----y --y!"
# Notes
# The letters are always given in lowercase, but they should be returned in the same
# case as in the original phrase (see example #3).
# All characters other than letters should always be returned (see example #4).
# Notes
# The letters are always given in lowercase, but they should be returned in the same
# case as in the original phrase (see example #3).
# All characters other than letters should always be returned (see example #4).

def hangman(word, letters):
    word = list(word)
    special=[" ","!","'",",","@",".","?"]
    output_list = []
    for i in range(len(word)):
        if word[i].upper() in letters or word[i].lower() in letters:
            output_list.append(word[i])
        elif word[i].isalpha and word[i] not in special:
            output_list.append("-")
        else:
            output_list.append(word[i])
    return "".join(output_list)


if __name__ == "__main__":
    print(hangman("helicopter", ["o", "e", "s"]))  # ➞ "-e---o--e-"
    print(hangman("tree", ["r", "t", "e"]))  # ➞ "tree"

    print(hangman("Python rules", ["a", "n", "p", "r", "z"]))  # ➞ "P----n r----"
    print(hangman("He's a very naughty boy!", ["e", "a", "y"])) # ➞ "-e"- a -e-y -a----y --y!"
