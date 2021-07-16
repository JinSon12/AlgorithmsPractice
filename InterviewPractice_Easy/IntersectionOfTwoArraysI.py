class Solution:
    def intersection_V1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    result.add(nums1[i])

        return result

    # using set.
    def intersection_V2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set()
        result = set()
        nums = []

        sm_len = min(len(nums1), len(nums2))
        lg_list = len(nums1) > len(nums2)

        if lg_list:
            s = set(nums1)
            nums = nums2
        elif lg_list == False and len(nums2) > 0:
            s = set(nums2)
            nums = nums1

        for i in range(sm_len):
            if nums[i] in s:
                result.add(nums[i])

        return result

    # realized that I misread some requirements,
    # no need to think about whether the lists are 0 in length or not.
    def intersection_V3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set(nums1)
        result = set()

        for i in nums2:
            if i in s:
                result.add(i)

        return result
