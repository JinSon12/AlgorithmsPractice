"""
https://leetcode.com/problems/range-sum-of-bst/submissions/
Range Sum BST 

- Key Insight: 
- Think about the basics of a BST. 
- node.left <= node.val <= node.right 이 재귀적으로 적용된 것. 

"""


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = []

        def dfs(node, low, high):
            if not node:
                return 0

            left = right = 0
            if low <= node.val <= high:
                left = dfs(node.left, low, high)
                right = dfs(node.right, low, high) + node.val

            elif node.val < low:
                right = dfs(node.right, low, high)

            elif node.val > high:
                left = dfs(node.left, low, high)

            return left + right

        return dfs(root, low, high)
