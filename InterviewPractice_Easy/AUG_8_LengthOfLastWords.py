# https://leetcode.com/problems/length-of-last-word/

"""
58. Length of Last Word

Input: s = "Hello World"
Output: 5


"""


class Solution:
    # 28ms, 78% 
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()

        return len(s[-1])
    
    # 12ms, more concise 
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip(" ").split(" ")[-1])
