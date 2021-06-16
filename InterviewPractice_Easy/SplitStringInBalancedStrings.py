# https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num = 0
        secondPointerInd = 0

        for i in range(len(s)):
            if s[secondPointerInd:i+1].count("L") == s[secondPointerInd:i+1].count("R"):
                secondPointerInd = i+1
                num += 1

        return num
