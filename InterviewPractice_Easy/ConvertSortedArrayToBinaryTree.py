# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # correct logic, but very very slow (148ms)
    def sortedArrayToBST_V1(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2
        print(mid)

        if len(nums) > 1:
            rootNode = TreeNode(nums[mid])
            rootNode.left = self.sortedArrayToBST(nums[:mid])
            rootNode.right = self.sortedArrayToBST(nums[mid+1:])
        else:
            return TreeNode(nums[mid])

    # removed the else statement. much faster (48ms)
    # b/c code for the else statement was doing the same thing,
    # but just didn't add the left, and right
    # but the first if statement (if not nums),
    # already checks for length of the array and acts accordingly.
    def sortedArrayToBST_V2(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2

        if len(nums) >= 1:
            rootNode = TreeNode(nums[mid])
            # slicing ex. [1:4] does not include 4.
            # therefore, nums parameter could be empty -> []
            rootNode.left = self.sortedArrayToBST(nums[:mid])
            rootNode.right = self.sortedArrayToBST(nums[mid+1:])
            return rootNode

        # else:
        #     return TreeNode(nums[mid])

    # shorter code, but reduces readability.
    def sortedArrayToBST_V3(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2

        if len(nums) >= 1:
            rootNode = TreeNode(nums[mid], self.sortedArrayToBST_V3(
                nums[:mid]), self.sortedArrayToBST_V3(nums[mid+1:]))
            return rootNode

    # sample 40ms

    def sortedArrayToBST_V4(self, nums: List[int]) -> TreeNode:
        return self.makeTree(nums)

    def makeTree(self, nums):
        # print(nums is None)
        if len(nums) != 0:
            m = int(len(nums)/2)
            # print(nums, m)
            node = TreeNode(val=nums[m])
            node.left = self.makeTree(nums[0:m])
            node.right = self.makeTree(nums[m+1:])
            return node
        else:
            return None


stn = Solution()
stn.sortedArrayToBST([-10, -3, 0, 5, 9])
