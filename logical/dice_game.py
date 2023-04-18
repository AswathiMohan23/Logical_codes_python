# 1.John is playing a dice game. The rules are as follows.
#
# Roll two dice.
# Add the numbers on the dice together.
# Add the total to your overall score.
# Repeat this for three rounds.
# But if you roll DOUBLES, your score is instantly wiped to 0 and your game ends immediately!
#
# Create a function that takes in a list of tuples as input, and return John's score after his game has ended.
#
# Examples
# dice_game([(1, 2), (3, 4), (5, 6)]) ➞ 21
#
# dice_game([(1, 1), (5, 6), (6, 4)]) ➞ 0
# dice_game([(4, 5), (4, 5), (4, 5)]) ➞ 27
# Notes
# Ignore all other tuples in the list if a throw happens to be doubles and go straight to returning 0.
# John only has two dice and will always give you outcomes for three rounds.

import random


def solution():
    dice_value = []
    dice_list=[]
    repeated_values=[]
    sum=0
    flag=0
    for j in range (0,3):
        random_num=random.randint(1,6)
        random_num2=random.randint(1,6)
        dice_tuple = (random_num,random_num2)

        dice_list.append(random_num)
        dice_list.append(random_num2)
        if random_num == random_num2:
            repeated_values.append(random_num)
            repeated_values.append(random_num2)
            flag=1
        dice_value.append(dice_tuple)
    print("dice values obtained by John : ",dice_value)
    if flag!=1:
        for i in dice_list:
            sum=sum+i
        print("sum is : ",sum)
    else:
        sum=0
        print("John's score is : ",sum," because John  got doubles ==> ",repeated_values)


if __name__ == "__main__":
    solution()


