"""
314. Binary Tree Vertical Order Traversal 

https://leetcode.com/problems/binary-tree-vertical-order-traversal/

"""

from collections import deque
from typing import Optional


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        nodes = {}
        res = []
        q = deque([[root, 0]])

        while q:
            node, ind = q.popleft()

            val = node.val
            if ind in nodes:
                nodes[ind].append(val)
            else:
                nodes[ind] = [val]

            if node.left:
                q.append([node.left, ind - 1])

            if node.right:
                q.append([node.right, ind + 1])

#         print(nodes)

        for k, v in sorted(nodes.items()):
            res.append(v)

        return res
