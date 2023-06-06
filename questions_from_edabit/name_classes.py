# Write a class called Name and create the following attributes given a first name and last name
# (as fname and lname):
#
# An attribute called fullname which returns the first and last names.
# An attribute called initials which returns the first letters of the first and last name.
# Put a . between the two letters.
# Remember to allow the attributes fname and lname to be accessed individually as well.
#
# Examples
# a1 = Name("john", "SMITH")
# a1.fname ➞ "John"
#
# a1.lname ➞ "Smith"
#
# a1.fullname ➞ "John Smith"
#
# a1.initials ➞ "J.S"
class Name:
    def __init__(self, fname, lname):
        self.fname = fname.capitalize()
        self.lname = lname
        self.fullname = fname.capitalize() + " " + lname.capitalize()
        self.initials = fname[0].capitalize() + "." + lname[0]


if __name__ == "__main__":
    a1 = Name("john", "SMITH")
    print(a1.fname)  # ➞ "John"
    print(a1.lname)  # ➞ "Smith"
    print(a1.fullname)  # ➞ "John Smith"
    print(a1.initials)  # ➞ "J.S"
