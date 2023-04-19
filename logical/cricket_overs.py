# In cricket, an over consists of six deliveries a bowler bowls from one end.
# Create a function that takes the number of balls bowled by a bowler and calculates the number
# of overs and  balls bowled by him/her. Return the value as a float, in the format overs.balls.
#
# Examples
# total_overs(2400) ➞ 400
#
# total_overs(164) ➞ 27.2
# # 27 overs and 2 balls were bowled by the bowler.
#
# total_overs(945) ➞ 157.3
# # 157 overs and 3 balls were bowled by the bowler.
#
# total_overs(5) ➞ 0.5
# Notes
# The number following the decimal point represents the balls remaining after the last over.
# Therefore, it will only ever have a value of 1-5.

def finding_overs(ball):
    count = 0
    over = 0
    for i in range(ball):
        count += 1
        if count == 6:
            over += 1
            count = 0
    print(over, ".", count)


if __name__ == "__main__":
    ball = 12
    finding_overs(ball)
