# In a board game, a piece may advance 1-6 tiles forward depending on the number rolled on a
# six-sided die. If you advance your piece onto the same tile as another player's piece, both
# of you earn a bonus.
#
# Can you reach your friend's tile number in the next roll? Create a function that takes
# your position a and your friend's position b and returns a boolean representation of whether it's
# possible to earn a bonus on any die roll.
#
# Examples
# possibleBonus(3, 7) ➞ true
#
# possibleBonus(1, 9) ➞ false
#
# possibleBonus(5, 3) ➞ false


def possibleBonus(person1, person2):
    return [True for i in range(1, 7) if person1+i == person2]

    # for i in range(1, 7):
    #     if person1 + i == person2:
    # return value


if __name__ == "__main__":
    # result = possibleBonus(5, 3)  # false
    # result=possibleBonus(3, 7) #true
    result=possibleBonus(1, 9)    #false
    if result == [True]:
        print("true")
    else:
        print("false")
