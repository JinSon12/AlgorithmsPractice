from collections import Counter


class Solution:
    def intersect_v1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sd = {}
        ld = {}
        result = []

        d1 = Counter(nums1)
        d2 = Counter(nums2)

        if len(d1) > len(d2):
            ld = d1
            sd = d2
        else:
            ld = d2
            sd = d1

        for k in sd:
            if k in ld:
                while sd[k] != 0 and ld[k] != 0:
                    result.append(k)
                    sd[k] -= 1
                    ld[k] -= 1

        return(result)
