# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

"""
1st t : JUL 27 

Key insight: 
- very similar to maxDepth Binary Tree question. 
- Problem : how to handle the degenerate cases (linked-list)? 
-           Also, what would be the best way to handle the subtrees(trees) that only has one side? (i.e. root.left == Null / root.right == Null)

- used height = 0 
- There can't be a height of 0 theoretically. (this is a starting point for the leaves)
- if either one side is returning 0 (meaning there is only one child of a root (either right or left child)), 
  then, we can just take the result from the side with the subtree and add 1 more to it. 
"""


from collections import deque
from InterviewPractice_Easy.Tree.TreeNode import TreeNode


class Solution:
    # recursive, 59%, 570ms
    def minDepth(self, root: TreeNode) -> int:
        if root:
            left_h = self.minDepth(root.left)
            right_h = self.minDepth(root.right)

            if left_h == 0:
                return 1 + right_h
            elif right_h == 0:
                return 1 + left_h

            return 1 + min(left_h, right_h)

        else:
            return 0

    # iterative, 94% ~ 98%, 464ms ~ 448ms
    def minDepth_iterative(self, root: TreeNode) -> int:
        if root is None:
            return 0

        deq = deque([root])
        height = 0

        # stop the loop once we see a node with no child.
        while deq:
            for _ in range(len(deq)):
                node = deq.popleft()

                if node.left == None and node.right == None:
                    return height + 1
                if node.left != None:
                    deq.append(node.left)
                if node.right != None:
                    deq.append(node.right)

            height += 1

        return height

    # fastest iterative solution
    #
    def minDepth_fastest_iterative(self, root: TreeNode) -> int:
        if root is None:
            return 0

        # appends depth, root
        node_queue = deque([(1, root), ])

        while node_queue:
            depth, node = node_queue.popleft()

            # puts children of a node into array
            children = [node.left, node.right]

            # if there are no children,
            if not any(children):
                return depth
            for c in children:
                if c:
                    node_queue.append((depth+1, c))
