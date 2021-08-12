
"""
529. Diameter fo Binary Tree 

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.



# [1,2,3,null, null,4,5,6,7,10,11,8,null,null,null,null,null,null,10,9]

KEY Insight: 
- need to keep a diameter variable that calculates the diameter for each node. 
(the distance to reach a node to another node)

- DFS 

"""

from typing import Optional
from InterviewPractice_Easy.Tree.TreeNode import TreeNode


class Solution:
    diameter = 0

    # dfs
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            # print(node.val, left, right)
            self.diameter = max(self.diameter, left + right + 2)
            return max(left, right) + 1

        dfs(root)

        return self.diameter
