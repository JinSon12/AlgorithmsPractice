# https://leetcode.com/problems/path-sum/submissions/
# 112. Path Sum

""" 
Key Insight: 
- Recursively go down to the leaf node, check if targetSum == root.val 
- the parameter targetSum would be targetSum - root.val 
- if targetSum == root.val, then we found a path! 

"""


class Solution:
    # 32ms, 98.9%
    def hasPathSum_recursive(self, root: TreeNode, targetSum: int) -> bool:
        # using recursive DFS
        if not root:
            return False

        if root.left == None and root.right == None:
            return targetSum == root.val

        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)

        # print(root, left, right)
        return left or right
