# Create a function that moves all capital letters to the front of a word.
#
# Examples
# capToFront("hApPy") ➞ "APhpy"
#
# capToFront("moveMENT") ➞ "MENTmove"
#
# capToFront("shOrtCAKE") ➞ "OCAKEshrt"


def capToFront(word):
    caps=[]
    small=[]
    output=[]

    result=[[i for i in word]]
    for i in word:
        if i == i.upper():
            caps.append(i)
        else:
            small.append(i)
    output.extend(caps)
    output.extend(small)
    return "".join(output)



if __name__=="__main__":
    print(capToFront("hApPy"))  #➞ "APhpy"