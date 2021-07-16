# https://leetcode.com/problems/relative-sort-array/

from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d1 = Counter(arr1)
        result = []

        for i in arr2:
            while i in d1 and d1[i] > 0:
                result.append(i)
                d1[i] -= 1
            d1.pop(i)

        for k in (sorted(d1.keys())):
            for j in range(d1[k]):
                result.append(k)

        return result
