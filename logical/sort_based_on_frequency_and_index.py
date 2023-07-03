# Given an integer array, in-place sort its element by their frequency and index. If two
# elements have different frequencies, then the one which has more frequency should come first;
# otherwise, the one which has less index should come first, i.e., the solution should
# preserve the relative order of the equal frequency elements.
#
# Input : [3, 3, 1, 1, 1, 8, 3, 6, 8, 7, 8]
# Output: [3, 3, 3, 1, 1, 1, 8, 8, 8, 6, 7]
#

def frequency(frequency):
    output = {}
    for i in range(len(frequency)):
        count = 1
        for j in range(len(frequency)):
            if i != j and frequency[i] == frequency[j]:
                count = count + 1
        output.update({frequency[i]: count})
    print(output)

    result = [i for i, j in output.items() for _ in range(j)]
    print(result)


if __name__ == "__main__":
    frequency([3, 3, 1, 1, 1, 8, 3, 6, 8, 7, 8])  # Output: [3, 3, 3, 1, 1, 1, 8, 8, 8, 6, 7]
