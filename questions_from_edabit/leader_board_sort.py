# Given an array of users, each defined by an object with the following properties:
# name, score, reputation create a function that sorts the array to form the correct leaderboard.
#
# The leaderboard takes into consideration the score of each user of course, but an emphasis is
# put on their reputation in the community, so to get the trueScore, you should add the reputation
# multiplied by 2 to the score.
#
# Once you know the trueScore of each user, sort the array according to it in descending order.
#
# Examples
# leaderboards([
#   { "name": "a", "score": 100, "reputation": 20 },
#   { "name": "b", "score": 90, "reputation": 40 },
#   { "name": "c", "score": 115, "reputation": 30 },
# ]) ➞ [
#   { "name": "c", "score": 115, "reputation": 30 },  # trueScore = 175
#   { "name": "b", "score": 90, "reputation": 40 },   # trueScore = 170
#   { "name": "a", "score": 100, "reputation": 20 }   # trueScore = 140
# ]




class LeaderBoard:
    def __init__(self):
        self.output_dict={}
        self.true_score=0

    def solution(self, input_list):
        result_dict={}
        for input_dict in input_list:
            self.output_dict=input_dict.copy()
            for key in input_dict:
                reputation = input_dict.get('reputation')
                score = input_dict.get('score')
                self.true_score=(reputation*2)+score
                self.output_dict.update({'true_score':self.true_score})
                result_dict.update({self.true_score:self.output_dict})
        result_dict=dict(sorted(result_dict.items(),reverse=True))
        for i in result_dict:
            print([result_dict.get(i)])


if __name__=="__main__":
    board=LeaderBoard()
    board.solution([
      { "name": "a", "score": 100, "reputation": 20 },
      { "name": "b", "score": 90, "reputation": 40 },
      { "name": "c", "score": 115, "reputation": 30 },
    ])
    # ➞ [
    #   { "name": "c", "score": 115, "reputation": 30 },  # trueScore = 175
    #   { "name": "b", "score": 90, "reputation": 40 },   # trueScore = 170
    #   { "name": "a", "score": 100, "reputation": 20 }   # trueScore = 140
    # ]

