# Given a sentence as txt, return True if any two adjacent words have this property:
# One word ends with a vowel, while the word immediately after begins with a vowel (a e i o u).
#
# Examples
# vowel_links("a very large appliance") ➞ True
#
# vowel_links("go to questions_from_edabit") ➞ True
#
# vowel_links("an open fire") ➞ False
#
# vowel_links("a sudden applause") ➞ False
# Notes
# You can expect sentences in only lowercase, with no punctuation.


def vowel_links(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    last,first = [],[]
    # first = []
    output=[]
    sentence = sentence.split(" ")
    for i in sentence:
        length = len(i)
        last.append(i[length - 1])
        first.append(i[0])
    for i in range(0, len(first) - 1):
        for j in range(i, len(last) - 1):
            if first[i] in vowels and last[j] in vowels:
                output.append("true")
            else:
                output.append("false")
    if "true" in output:
        return True
    else:
        return False


if __name__ == "__main__":
    print(vowel_links("a very large appliance"))
    print(vowel_links("go to questions_from_edabit"))
    print(vowel_links("an open fire"))
    print(vowel_links("a sudden applause"))


