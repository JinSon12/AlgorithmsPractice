# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict

"""
49. Group Anagrams

"""


class Solution:
    # 88ms ~ 100ms, 96.6%
    # same idea, approach as the fastest solution
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        if len(strs) == 0:
            return [""]

        d = defaultdict(list)

        for word in strs:
            sWord = "".join(sorted(word))
            d[sWord].append(word)

        return d.values()
