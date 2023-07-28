# Create a function that will build a staircase using the underscore _ and hash # symbols.
# A positive value denotes the staircase's upward direction and downwards for a negative value.
#
# Examples
# staircase(3) ➞ "__#\n_##\n###"
# __#
# _##
# ###
#
# staircase(7) ➞ "______#\n_____##\n____###\n___####\n__#####\n_######\n#######"
# ______#
# _____##
# ____###
# ___####
# __#####
# _######
# #######
#
# staircase(2) ➞ "_#\n##"
# _#
# ##
#
# staircase(-8) ➞ "########\n_#######\n__######\n___#####\n____####\n_____###\n______##\n_______#"
# ########
# _#######
# __######
# ___#####
# ____####
# _____###
# ______##
# _______#

def staircase(num):
    step = '#'
    underscore='_'
    if num >0:
        for i in range(1, num+1):
            count=num-i
            print(underscore * count,end=" ")
            print(step*i)
    else:
        num=num*-1
        for i in range(0, num):
            count=num-i
            print(step * count,end=" ")
            print(underscore*i)



if __name__ == '__main__':
    print("\t\tnegative input : \n")
    staircase(-8)
    print("\t\tpositive input : \n")
    staircase(8)

