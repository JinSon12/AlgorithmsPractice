# https://leetcode.com/problems/assign-cookies/ 

"""
Assign Cookies. 

Greedy + sorting 

"""


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        cookiePos = 0
        childP = 0
        # counter = 0

        while childP < len(g) and cookiePos < len(s):
            child = g[childP]
            # print(child, cookiePos, s[cookiePos])
            if cookiePos < len(s) and child <= s[cookiePos]:
                # counter += 1 removing this decreases the runtime by half.
                childP += 1

            cookiePos += 1

        return childP
