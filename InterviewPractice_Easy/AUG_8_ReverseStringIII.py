# https://leetcode.com/problems/reverse-words-in-a-string-iii/

"""
557. Reverse Words in a String III

- use [::-1] to reverse string. 
- list slicing is much faster as it is implemented using C inside python
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for word in s.split():
            res.append(word[::-1])

        return " ".join(res)
