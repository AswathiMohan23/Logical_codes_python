# Given two strings ransomNote and magazine,return true if ransomNote can be constructed by using the letters
# from magazine and false otherwise Each letter in magazine can  only be used
# once in ransomNote.
#
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution:
    output = []

    def solution(self, ransomNote, magazine):
        self.ransom_list = list(ransomNote)
        for i in ransomNote:
            if i in magazine:
                self.output.append(i)
        if len(self.output) == len(self.ransom_list):
            print("True !!! note can be constructed")
        else:
            print("False !!! note cannot be constructed")


if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "aab"
    print("input : ransom = ", ransomNote, " , magazine = ", magazine)
    obj = Solution()
    obj.solution(ransomNote, magazine)
