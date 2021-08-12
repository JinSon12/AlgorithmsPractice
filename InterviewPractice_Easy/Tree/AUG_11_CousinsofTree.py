# https://leetcode.com/problems/cousins-in-binary-tree/

"""
993. Cousins in Binary Tree

KEY Insight: 
- using BFS 
- save element(node, parent, height) into deque
- bfs 

return if height is the same but parent is different. 

"""


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        res = []

        queue = deque([(root, None, 0)])  # node, parent, height

        while queue:
            node, parent, height = queue.popleft()

            if node.val == x or node.val == y:
                res.append((node, parent, height))

            if node.left:
                queue.append((node.left, node, height + 1))

            if node.right:
                queue.append((node.right, node, height + 1))

        if res[0][2] == res[1][2] and res[0][1] != res[1][1]:
            return True
