
from InterviewPractice_Easy.Tree.TreeNode import TreeNode
# https://leetcode.com/problems/invert-binary-tree/submissions/
"""
JUL_29 

226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

Key Insight: 
- Use recursion. 
- left -> right, right -> left all the way down!! 

Because of recursion, 
O(h) function calls will be placed on the stack in the worst case, where 
h is the height of the tree. Because h∈O(n), the space complexity is O(n).
"""


class Solution:

    # 32ms, 65.88%
    # Memory Usage: 14.1 MB, less than 91.09% of Python3 online submissions for Invert Binary Tree.
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None

        if root.left == None and root.right != None:
            root.left = self.invertTree(root.right)
            root.right = None
            return root

        if root.right == None and root.left != None:
            root.right = self.invertTree(root.left)
            root.left = None
            return root

        if root.right == None and root.left == None:
            return root

        root.right, root.left = self.invertTree(
            root.left), self.invertTree(root.right)
        return root

    # 24ms, 96.99%
    def invertTree_recursive_revised(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None

        root.right, root.left = self.invertTree(
            root.left), self.invertTree(root.right)
        return root

    # slower, 40ms, but WAY CONCISE!!!
    def invertTree_concise(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        return TreeNode(val=root.val, left=self.invertTree(root.right), right=self.invertTree(root.left))
