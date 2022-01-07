"""
Count Good Nodes in Binary Tree

https://leetcode.com/problems/count-good-nodes-in-binary-tree/

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countGoodNodesInBinaryTree(root: TreeNode):
    def dfs(node, maxNode):
        if not node:
            return 0

        maxNode = max(maxNode, node.val)

        left = dfs(node.left, maxNode)
        right = dfs(node.right, maxNode)

        count = 0
        if node.val >= maxNode:
            count += 1

        return left + right + count

    return dfs(root, root.val)
