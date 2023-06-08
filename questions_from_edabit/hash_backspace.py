# Suppose a hash # represents the BACKSPACE key being pressed. Write a function
# that transforms a string containing # into a string without any #.
# 
# Examples
# erase("he##l#hel#llo") ➞ "hello"
# 
# erase("major# spar##ks") ➞ "majo spks"
# 
# erase("si###t boy") ➞ "t boy"
# 
# erase("####") ➞ ""
# Notes
# In addition to characters, backspaces can also remove whitespaces.
# If the number of hashes exceeds the previous characters, remove those previous characters 
# entirely (see example #3).
# If there only exist backspaces, return an empty string (see example #4).

def erase(word):
    output = []
    for i in range(len(list(word))):
        output.append(word[i])
        if "#" in output:
            output.remove("#")
            if len(output) != 0:
                output.pop()
    return "".join(output)


if __name__ == "__main__":
    print(erase("he##l#hel#llo"))  # ➞ "hello"
    print(erase("major# spar##ks"))  # ➞ "majo spks"
    print(erase("si###t boy"))  # ➞ "t boy"
    print(erase("####"))  # ➞ ""
