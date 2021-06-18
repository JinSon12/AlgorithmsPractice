# https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []

        for i in range(0, len(nums)):
            # o(n)
            res.insert(index[i], nums[i])

        return res

    def createTargetArray2(self, nums, index):
        length = len(nums)
        target = []
        for i in range(length):
            if index[i] >= length:
                target.append(nums[i])
            else:
                target.insert(index[i], nums[i])
        return target

    def createTargetArray3(self, nums: List[int], index: List[int]) -> List[int]:
        for i in range(len(index)):
            for j in range(0, i):
                if index[j] >= index[i]:
                    index[j] += 1
        target = [None] * len(index)
        for i in range(len(index)):
            target[index[i]] = nums[i]
        return target
