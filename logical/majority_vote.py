# Create a function that returns the majority vote in a list.
# A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).
#
# Examples
# majority_vote(["A", "A", "B"]) ➞ "A"
#
# majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"
#
# majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None
# Notes
# The frequency of the majority element must be strictly greater than 1/2.
# If there is no majority element, return None.
# If the list is empty, return None.


def majority_vote(votes):
    value=[]
    input_list=[]
    input_list.extend(votes)
    given_list=[]
    given_list.extend(votes)

    length=len(votes)//2
    [value.append(i) for i in input_list if i not in value] # now value will have each name only once
    count=0
    output= {}

    for i in value:
        for j in range(0,len(given_list)):
            if i ==given_list[j]:
                count=count+1
        output.update({i: count})
        count=0

    for key in output:
        if output[key]>length:
            return key
    return None


if __name__ == "__main__":
    print(majority_vote(["A", "A", "B"])) #➞ "A"
    print(majority_vote(["A", "A", "A", "B", "C", "A"])) # ➞ "A"
    print(majority_vote(["A", "B", "B", "A", "C", "C"])) # ➞ None