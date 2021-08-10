# https://leetcode.com/problems/reverse-string/

""" 
344. Reverse String

KEY insight 
- library 사용 
- two pointers 
- 재귀 

"""


class Solution:
    def reverseString_tp(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) <= 1:
            return s

        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return s
