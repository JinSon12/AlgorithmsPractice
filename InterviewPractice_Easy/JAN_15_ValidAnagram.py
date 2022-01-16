"""
https://leetcode.com/problems/valid-anagram/submissions/


"""


class Solution:

    # TC O(n log n)
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    # TC O(n)
    def isAnagram_map(self, s: str, t: str) -> bool:
        ms = {}
        mt = {}

        if len(s) != len(t):
            return False

        for c in s:
            if c not in ms:
                ms[c] = 1
            else:
                ms[c] += 1

        for c in t:
            if c not in mt:
                mt[c] = 1
            else:
                mt[c] += 1

        return ms == mt
