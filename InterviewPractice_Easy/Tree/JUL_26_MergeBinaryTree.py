# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from InterviewPractice_Easy.Tree.TreeNode import TreeNode

"""
617. Merge Two Binary Trees 


https://leetcode.com/problems/merge-two-binary-trees/

"""


class Solution:

    # solved using DFS - recursion.
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 == None and root2 != None:
            return root2
        elif root1 != None and root2 == None:
            return root1
        elif root1 == None and root2 == None:
            return None

        # print(root1, root2)
        # Highlight : we are not transferring the saved values to some other nodes,
        # we just need to change the Tree 1's nodes (by adding the Tree 2's nodes)
        root1.val = root1.val + root2.val

        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1

    # Notice the logic for handling None values.
    # Cleaner than mine!!!
    def mergeTrees_FastestSolution(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 == None:
            return root2

        if root2 == None:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1
