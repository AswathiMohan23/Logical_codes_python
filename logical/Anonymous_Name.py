# You are in the process of creating a chat application and want to add an
# anonymous name feature. This anonymous name feature will create an alias
# that consists of two capitalized words beginning with the same letter as
# the users first name.
#
# Create a function that determines if the list of users is mapped to a list
# of anonymous names correctly.
#
# Examples
# is_correct_aliases(["Adrian M.", "Harriet S.", "Mandy T."], ["Amazing Artichoke", "Hopeful Hedgehog", "Marvelous Mouse"]) ➞ True
#
# is_correct_aliases(["Rachel F.", "Pam G.", "Fred Z.", "Nancy K."], ["Reassuring Rat", "Peaceful Panda", "Fantastic Frog", "Notable Nickel"]) ➞ True
#
# is_correct_aliases(["Beth T."], ["Brandishing Mimosa"]) ➞ False
# Both words in "Brandishing Mimosa" should begin with a "B" - "Brandishing Beaver" would do the trick.

def is_correct_aliases(input_list, alias_list):
    letters_in_input_list = []
    letters_in_alias_list = []
    letters_in_alias_name = []
    letters_in_alias_second_name = []
    for i in input_list:
        elements = i.split(" ")

        for j in elements:
            for k in range(len(j)):
                letters_in_input_list.append(j[0])
                break
            break
    for i in alias_list:
        elements = i.split(" ")

        for j in elements:
            for k in range(len(j)):
                letters_in_alias_list.append(j[0])
                break
            break
    elements = list("".join(alias_list))
    if letters_in_alias_list == letters_in_input_list:
        for j in range(len(elements)):
            value = elements[j]
            for k in value:
                if k.isupper():
                    letters_in_alias_name.append(k)
        if len(letters_in_alias_name) > 2:
            for i in range(len(letters_in_alias_name)):
                if i % 2 == 0 or i == 0:
                    letters_in_alias_second_name.extend(letters_in_alias_name[i])
        else:
            first=letters_in_alias_name[0]
            second=letters_in_alias_name[1]
            if first == second:
                letters_in_alias_second_name.extend(letters_in_alias_name[0])

        if letters_in_input_list == letters_in_alias_second_name:
            return True
        else:
            return False


if __name__ == "__main__":
    # print(is_correct_aliases(["Adrian M.", "Harriet S.", "Mandy T."],
    #                    ["Amazing Artichoke", "Hopeful Hedgehog", "Marvelous Mouse"])) # ➞ True
    # print(is_correct_aliases(["Beth T."], ["Brandishing Mimosa"]))  # false
    # print(is_correct_aliases(["Rachel F.", "Pam G.", "Fred Z.", "Nancy K."],["Reassuring Rat", "Peaceful Panda",
    #                             "Fantastic Frog", "Notable Nickel"]))# ➞ True

    print("Amazing Artichoke".split(" "))
