# https://leetcode.com/problems/subtree-of-another-tree/

"""
572. Subtree of Another Tree

- dfs

worst case O(v + e)
best case O(smaller tree's v + e)

"""

from typing import Optional
from InterviewPractice_Easy.Tree.TreeNode import TreeNode
import timeit


class Solution:
    # longer but faster (90~110)
    def isSubtree_v1(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return False

            left = dfs(node.left)
            right = dfs(node.right)

            if left or right:
                return True

            # print(node.val)
            if node.val == subRoot.val:
                res = checkTrees(node, subRoot)
                # print("rews", res)
                return res

        def checkTrees(n1, n2):
            if not n1 and not n2:
                return True

            # print(n1.val, n2.val)

            if not n1 and n2 or n1 and not n2:
                return False

            if n1.val == n2.val:
                # print("n1 equal n2", n1.val, n2.val)
                left = checkTrees(n1.left, n2.left)
                right = checkTrees(n1.right, n2.right)

                # print(left, right)

                return left and right

        return dfs(root)

    # recursion, but more concise, slower (150~)
    def isSubtree_concise(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if self.isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p == q

    # good solution
    def isSubtree_v2(self, a, b):
        if not b:
            return True

        def checkTree(root1, root2):
            if not root1 and not root2:
                return True
            elif root1 and not root2 or root2 and not root1:
                return False

            if root1.val != root2.val:
                return False

            return checkTree(root1.left, root2.left) and checkTree(root1.right, root2.right)

        def dfs(s, t):
            if not s:
                return False

            if s.val == t.val and checkTree(s, t):
                return True

            return dfs(s.left, t) or dfs(s.right, t)

        return dfs(a, b)
