# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    """
    worst case o(n^2)
    """

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        # alternatively, can use max(nums)
        # O(n)
        max_val = max(nums)
        max_idx = nums.index(max_val)
        # max_idx = self.findMax(nums)
        node = TreeNode(nums[max_idx])
        node.left = self.constructMaximumBinaryTree(nums[:max_idx])
        node.right = self.constructMaximumBinaryTree(nums[max_idx+1:])

        return node

    def findMax(self, arr: List[int]):
        maxVal = float('-inf')
        pos = 0

        # O(n)
        for i in range(len(arr)):
            if arr[i] > maxVal:
                maxVal = arr[i]
                pos = i

        return (pos)
