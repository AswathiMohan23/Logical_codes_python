# Write a Composer class that has three instance variables:
#
# name
# dob
# country
# Add an additional class variable .count which counts the total number of instances created.
#
# Examples
# # Just finished writing the Composer class
# Composer.count ➞ 0
#
# c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
# Composer.count ➞ 1
#
# c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
# c3 = Composer("Johannes Brahms", 1833, "Germany")
# Composer.count ➞ 3

class Composer:
    counter = 0

    def __init__(self, name=None, dob=0, country=None):
        Composer.counter += 1
        self.name = name
        self.dob = dob
        self.country = country
        self.count = Composer.counter


if __name__ == "__main__":
    # Just finished writing the Composer class
    # Composer.count ➞ 0

    c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
    print(c1.count)  # ➞ 1

    c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
    print(c2.count)  # ➞ 3
    print(c1.counter)

    # c3 = Composer("Johannes Brahms", 1833, "Germany")
    # print(c3.count)  # ➞ 3
