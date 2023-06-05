# Given a sentence as txt, return True if any two adjacent words have this property:
# One word ends with a vowel, while the word immediately after begins with a vowel (a e i o u).
#
# Examples
# vowel_links("a very large appliance") ➞ True
#
# vowel_links("go to edabit") ➞ True
#
# vowel_links("an open fire") ➞ False
#
# vowel_links("a sudden applause") ➞ False
# Notes
# You can expect sentences in only lowercase, with no punctuation.


def vowel_links(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    input_string = input_string.split(" ")

    for i in range(0, len(input_string)):
        if input_string[i][-1] in vowels and input_string[i + 1][1] in vowels:
            return True
        else:
            return False


if __name__ == "__main__":
    print(vowel_links("a very large appliance"))  # ➞ True
    print(vowel_links("go to edabit"))  # ➞ True
    print(vowel_links("an open fire"))  # ➞ False
