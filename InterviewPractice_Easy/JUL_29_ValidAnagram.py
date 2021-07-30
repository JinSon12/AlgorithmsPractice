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
