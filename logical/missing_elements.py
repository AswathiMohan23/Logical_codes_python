# you are given two lists. The elements in lst1 threw a party and started to mix around.
# However, one of the elements got lost! Your task is to return the element which was lost.
#
# Examples
# missing([1, 2, 3, 4, 5, 6, 7, 8], [1, 3, 4, 5, 6, 7, 8]) ➞ 2
#
# missing([True, True, False, False, True], [False, True, False, True]) ➞ True
#
# missing(["Jane", "is", "pretty", "ugly"], ["Jane", "is", "pretty"]) ➞ "ugly"
#
# missing(["different", "types", "5", 5, [5], (5,)], ["5", "different", [5], "types", 5]) ➞ (5,)
# Notes
# Assume that the first list always contains 1 or more elements.
# Elements are always lost.
# An element can also have duplicates.


def missing(list1, list2):
    for i in list1:
        if i not in list2:
            return i


def missing_boolean(list1, list2):
    for i in list1:
        for j in list2:
            if i !=j:
                return i



if __name__=="__main__":
    print(missing([1, 2, 3, 4, 5, 6, 7, 8], [1, 3, 4, 5, 6, 7, 8])) #➞ 2
    print(missing_boolean([True, True, False, False, True], [False, True, False, True]))# ➞ True
    print(missing(["Jane", "is", "pretty", "ugly"], ["Jane", "is", "pretty"]))# ➞ "ugly"
    print(missing(["different", "types", "5", 5, [5], (5,)], ["5", "different", [5], "types", 5]))# ➞ (5,)

