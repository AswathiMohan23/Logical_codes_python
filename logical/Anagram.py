# 2.Write a function that returns True if a given name can generate an array of words.
#
# Examples
# anagram("Justin Bieber", ["injures", "ebb", "it"]) ➞ True
#
# anagram("Natalie Portman", ["ornamental", "pita"]) ➞ True
#
# anagram("Jeff Goldblum", ["jog", "meld", "bluffs"]) ➞ False
# # "s" does not exist in the original name
# Notes
# Each letter in the name may only be used once.
# All letters in the name must be used.

def anagram(word, array):
    output=[]
    word = list(word.lower())
    word.remove(" ")
    array = list("".join(array))
    # output = [i for i in array if i in word]
    # return True if array == output else False

    for i in array:
        if i in word:
            output.append(i)
            word.remove(i)
    if array == output:
        return True
    else:
        return False


if __name__ == "__main__":
    print(anagram("Justin Bieber", ["injures", "ebb", "it"]))  # ➞ True
    print(anagram("Justin Bieber", ["injures", "ebb"," "]))  # ➞ False
    print(anagram("Natalie Portman", ["ornamental", "pita"]))  # ➞ True
    print(anagram("Jeff Goldblum", ["jog", "meld", "bluffs"]))  # ➞ False
