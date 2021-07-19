class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d2 = {}

        # initialize all the indices
        # and default the values to -1
#         for el in nums2:
#             d2[el] = -1

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                d2[(stack.pop())] = nums2[i]

            stack.append(nums2[i])

        # return([d2[x] for x in nums1])
        # use .get(x, -1), to give -1 if the key x doesn't exist in the dictionary.
        return([d2.get(x, -1) for x in nums1])
