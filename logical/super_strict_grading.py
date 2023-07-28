# Given a dictionary of student names and a list of their test scores over the semester,
# return a list of all the students who passed the course (in alphabetical order). However,
# there is one more thing to mention: the pass mark is 100% in everything!
#
# Examples
# who_passed({
#   "John" : ["5/5", "50/50", "10/10", "10/10"],
#   "Sarah" : ["4/8", "50/57", "7/10", "10/18"],
#   "Adam" : ["8/10", "22/25", "3/5", "5/5"],
#   "Barry" : ["3/3", "20/20"]
# }) ➞ ["Barry", "John"]
#
# who_passed({
#   "Zara" : ["10/10"],
#   "Kris" : ["30/30"],
#   "Charlie" : ["100/100"],
#   "Alex" : ["1/1"]
# }) ➞ ["Alex", "Charlie", "Kris", "Zara"]
#
# who_passed({
#   "Zach" : ["10/10", "2/4"],
#   "Fred" : ["7/9", "2/3"]
# }) ➞ []

def who_passed(results):
    output = []
    for j in results:
        fail = 0
        each_result = results.get(j)
        for i in each_result:
            value = i.split("/")
            if int(value[0]) / int(value[1]) != 1:
                fail = fail + 1
                break
        if fail == 0:
            output.append(j)
    output.sort()
    return output


if __name__ == "__main__":
    print(who_passed({
        "John": ["5/5", "50/50", "10/10", "10/10"],
        "Sarah": ["4/8", "50/57", "7/10", "10/18"],
        "Adam": ["8/10", "22/25", "3/5", "5/5"],
        "Barry": ["3/3", "20/20"]
    }))  # ➞ ["Barry", "John"]

    print(who_passed({
        "Zara": ["10/10"],
        "Kris": ["30/30"],
        "Charlie": ["100/100"],
        "Alex": ["1/1"]
    }))  # ➞ ["Alex", "Charlie", "Kris", "Zara"]

    print(who_passed({
        "Zach": ["10/10", "2/4"],
        "Fred": ["7/9", "2/3"]
    }))  # ➞ []
