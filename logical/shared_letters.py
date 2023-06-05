# Create a function that takes in two words as input and returns a
# list of three elements, in the following order:
#
# Shared letters between two words.
# Letters unique to word 1.
# Letters unique to word 2.
# Each element should have unique letters, and have each letter be alphabetically sorted.
#
# Examples
# letters("sharp", "soap") ➞ ["aps", "hr", "o"]
#
# letters("board", "bored") ➞ ["bdor", "a", "e"]
#
# letters("happiness", "envelope") ➞ ["enp", "ahis", "lov"]
# letters("kerfuffle", "fluffy") ➞ ["flu", "ekr", "y"]
# # Even with multiple matching letters (e.g. 3 f's), there should
# # only exist a single "f" in your first element.
#
# letters("match", "ham") ➞ ["ahm", "ct", ""]
# # "ham" does not contain any letters that are not found already
# # in "match".
# Notes
# Both words will be in lower case.
# You do not have to worry about punctuation, all words only have letters from [a-z].
# If an element contains no letters, return an empty string (see last example).


def sort_and_join(word, output):
    word.sort()
    output.append("".join(word))


def letters(first, second):
    common = []
    output = []
    letters_in_first = []
    first = list(first)
    second = list(second)
    for i in first:
        if i in second:
            common.append(i)
            second.remove(i)
        else:
            letters_in_first.append(i)
    sort_and_join(common, output)
    sort_and_join(letters_in_first, output)
    sort_and_join(second, output)
    print(output)


if __name__ == "__main__":
    letters("sharp", "soap")  # ➞ ["aps", "hr", "o"]
    letters("match", "ham")# ➞ ["ahm", "ct", ""]
