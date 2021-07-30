# https://leetcode.com/problems/string-matching-in-an-array/

"""
1408. String Matching in an Array

Key Insight: 
- Brute Force, 
- sort the words array by the length of the words in ascending order. 
- if a word is a substring of another word, it must be shorter in length. 
- Use "in" operator, for string/list = o(n), set/dict => avg o(1), worst o(n)

- 
"""

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # sort by the length of the words
        words.sort(key=lambda x: len(x))

        res = set()

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    res.add(words[i])

        return res
