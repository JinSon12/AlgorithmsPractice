# https://leetcode.com/problems/symmetric-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from InterviewPractice_Easy.Tree.TreeNode import TreeNode
from typing import Deque


class Solution:

    # recursive solution
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isSubtreeSame(root.left, root.right)

    def isSubtreeSame(self, left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        return left.val == right.val and self.isSubtreeSame(left.left, right.right) and self.isSubtreeSame(left.right, right.left)

    # Iterative Solution
    def isSymmetric_iterative(self, root: TreeNode) -> bool:
        deq = Deque([(root.left, root.right)])

        while deq:
            left, right = deq.popleft()
            if left == None and right == None:
                continue
            elif left == None or right == None:
                return False
            elif left.val != right.val:
                return False

            deq.append((left.left, right.right))
            deq.append((left.right, right.left))

        return True
