# Run–length encoding (RLE) is a simple form of lossless data compression that runs on sequences
# with the same value occurring many consecutive times. It encodes the sequence to store only a
# single value and its count.
#
# Input: 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
# Output: '12W1B12W3B24W1B14W'
# Explanation: String can be interpreted as a sequence of twelve W’s, one B, twelve W’s, three B’s,
# and so on..

def counting_letters(count, i, output):
    result = str(count) + i
    output.append(result)


def encoding(param):
    value = list(param)
    output = []
    count = 0
    for i in range(0, len(value) - 1):
        if value[i] == value[i + 1]:
            count = count + 1
        else:
            count = count + 1
            counting_letters(count, value[i], output)
            count = 0
    count = count + 1
    counting_letters(count, value[i], output)
    return "".join(output)


if __name__ == "__main__":
    print(encoding('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'))
    # Output: '12W1B12W3B24W1B14W'
