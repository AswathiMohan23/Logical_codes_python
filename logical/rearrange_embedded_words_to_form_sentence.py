# Given a sentence with numbers representing a word's location embedded within each word,
# return the sorted sentence.
#
# Examples
# rearrange("is2 Thi1s T4est 3a") ➞ "This is a Test"
#
# rearrange("4of Fo1r pe6ople g3ood th5e the2") ➞ "For the good of the people"
#
# rearrange(" ") ➞ " "
# Notes
# Only the integers 1-9 will be used.

def rearrange(sentence):
    if sentence == " ":
        print('" "')
    else:
        output = {}
        sentence = "".join(sentence)
        sentence = sentence.split(" ")
        for i in range(0, len(sentence)):
            value = sentence[i]

            for j in range(0, len(value)):
                if value[j].isalpha():
                    pass
                else:
                    output.update({value[j]: value})
        keys = list(output.keys())
        keys.sort()
        answer = ""
        for i in keys:
            result = output.get(i)
            for j in result:
                if i == j:
                    pass
                else:
                    answer = answer + j
            answer = answer + " "
        print(answer)


if __name__ == "__main__":
    rearrange("is2 Thi1s T4est 3a")  # ➞ "This is a Test"
    rearrange("4of Fo1r pe6ople g3ood th5e the2")  # ➞ "For the good of the people"
    rearrange(" ")  # ➞ " "
