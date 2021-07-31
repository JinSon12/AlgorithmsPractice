from typing import Collection

"""
Think about the dictionary version as well. s
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        list1 = [x for x in s]
        list2 = [x for x in t]

        list1.sort()
        list2.sort()

        if list1 == list2:
            return True

    # simpler, concise, faster solution 16ms
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Collection.Counter(s)
        count_t = Collection.Counter(t)
        return count_s == count_t

