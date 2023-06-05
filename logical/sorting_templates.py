# The function is given two strings t - template, s - to be sorted.
# Sort the characters in s such that if the character is present in t then it is sorted according
# to the order in t and other characters are sorted alphabetically after the ones found in t.
#
# Examples
# custom_sort("edc", "abcdefzyx") ➞ "edcabfxyz"
#
# custom_sort("fby", "abcdefzyx") ➞ "fbyacdexz"
#
# custom_sort("", "abcdefzyx") ➞ "abcdefxyz"
#
# custom_sort("", "") ➞ ""
# Notes
# The characters in t and s are all lower-case.

def sorting(word,length):
    for i in range(length):
        for j in range(0, length - i - 1):
            if word[j] > word[j + 1]:
                (word[j + 1], word[j]) = (word[j], word[j + 1])
    return word


def custom_sort(template, word):
    output=[]
    word_list=list(word)
    template_list=list(template)
    sorted_word=sorting(word_list,len(word_list))
    sorted_template=sorting(template_list,len(template_list))
    if template=="":
        print("".join(sorted_word))
    else:

        [sorted_word.remove(i) for i in sorted_template for j in sorted_word if i==j]
        output.append(template)
        output.extend(sorted_word)
        output="".join(output)
        print(output)


if __name__=="__main__":
    custom_sort("edc", "abcdefzyx") # ➞ "edcabfxyz"
    custom_sort("fby", "abcdefzyx")# ➞ "fbyacdexz"

    custom_sort("", "abcdefzyx") #➞ "abcdefxyz"
    custom_sort("", "") #➞ ""