# Create a function to check if a candidate is qualified in an imaginary coding interview of an
# imaginary tech startup.The criteria for a candidate to be qualified in the coding interview is:
# The candidate should have complete all the questions.
# The maximum time given to complete the interview is 120 minutes.
# The maximum time given for very easy questions is 5 minutes each.
# The maximum time given for easy questions is 10 minutes each.
# The maximum time given for medium questions is 15 minutes each.
# The maximum time given for hard questions is 20 minutes each.
# If all the above conditions are satisfied, return "qualified", else return "disqualified".
#
# You will be given a list of time taken by a candidate to solve a particular question and the total time
# taken by the candidate to complete the interview.
#
# Given a list , in a true condition will always be in the format
# [very easy, very easy, easy, easy, medium, medium, hard, hard].
#
# The maximum time to complete the interview includes a buffer time of 20 minutes.
#
# Examples
# interview([5, 5, 10, 10, 15, 15, 20, 20], 120) ➞ "qualified"
#
# interview([2, 3, 8, 6, 5, 12, 10, 18], 64) ➞  "qualified"
#
# interview([5, 5, 10, 10, 25, 15, 20, 20], 120) ➞ "disqualified"
# # Exceeded the time limit for a medium question.
#
# interview([5, 5, 10, 10, 15, 15, 20], 120) ➞ "disqualified"
# # Did not complete all the questions.
#
# interview([5, 5, 10, 10, 15, 15, 20, 20], 130) ➞ "disqualified"
# # Solved all the questions in their respected time limits but exceeded the total time limit of the interview

# [very easy-5, very easy-5, easy-10, easy-10, medium-15, medium-15, hard-20, hard-20].

# def output_value(output):
#     return "qualified" if output == 0 else "disqualified"
#

def interview(individual_time, total_time):
    if total_time > 120 or len(individual_time)!=8:
        return "disqualified"

    else:
        for i in range(0, 2):
            if individual_time[i] <= 5:
                pass
            else:
                return "disqualified"
        for i in range(2, 4):
            if individual_time[i] <= 10:
                pass
            else:
                return "disqualified"

        for i in range(4, 6):
            if individual_time[i] <= 15:
                pass
            else:
                return "disqualified"
        for i in range(6, 8):
            if individual_time[i] <= 20:
                pass
            else:
                return "disqualified"

    return "qualified"


if __name__ == "__main__":
    print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))# qualified
    print(interview([5, 5, 10, 10, 15, 15, 20, 30], 120)) # disqualified
    print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64))     # "qualified"
    print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120)) # "disqualified"
    print(interview([5, 5, 10, 10, 15, 15, 20], 120)) # "disqualified"
