# Write a function that inverts the keys and values of a dictionary.
#
# Examples
# invert({ "z": "q", "w": "f" })
# ➞ { "q": "z", "f": "w" }
#
# invert({ "a": 1, "b": 2, "c": 3 })
# ➞ { 1: "a", 2: "b", 3: "c" }
#
# invert({ "zebra": "koala", "horse": "camel" })
# ➞ { "koala": "zebra", "camel": "horse" }

def invert(dict1):
    output = {}
    for i in dict1:
        output.update({dict1.get(i): i})
    return output


if __name__ == "__main__":
    print(invert({"z": "q", "w": "f"}))  # ➞ { "q": "z", "f": "w" }
    print(invert({"a": 1, "b": 2, "c": 3}))  # ➞ { 1: "a", 2: "b", 3: "c" }
    print(invert({"zebra": "koala", "horse": "camel"}))  # ➞ { "koala": "zebra", "camel": "horse" }
