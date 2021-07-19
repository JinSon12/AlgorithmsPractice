# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    """
    O(n)
    """

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        stack = []

        for num in nums:
            node = TreeNode(num)

            while stack and stack[-1].val < num:
                node.left = stack.pop()

            # 이때 stack에 원소가 존재한다면, stack[-1].val >= num
            if stack:
                stack[-1].right = node

            stack.append(node)

        return stack[0]

    """
    worst case o(n^2): in the case of fully sorted array. 
    """

    def constructMaximumBinaryTree_recursive(self, nums: List[int]) -> TreeNode:
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


stn = Solution()

result = stn.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
print(result)
