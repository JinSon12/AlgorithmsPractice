# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/


"""
Key Insight: 
- root itselt would be of height 1 
- every time we go a level down (recursive), we want to... 
- get the max height of each recursive call + 1 
"""
from collections import deque
from InterviewPractice_Easy.Tree.TreeNode import TreeNode


class Solution:

    # 76.7% faster, 40ms
    # 92.9% faster, 36ms
    def maxDepth_recursive(self, root: TreeNode) -> int:
        if root == None:
            return 0

        left_h = self.maxDepth(root.left) + 1
        right_h = self.maxDepth(root.right) + 1

        # print(root.val, left_h, right_h)

        return max(left_h, right_h)

    # recursive, but way cleaner solution!
    """
    Key Insight: if root exists, then return the max of left depth and right depth + 1 (the root)
    else (if the root is None), return 0 
    """

    def maxDepth_recursive_cleaner(self, root: TreeNode) -> int:
        if root:
            return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
        else:
            return 0

    # avg 37 ms
    # code looks longer compared to recursive.
    """
    Key Insight: 
    - 파이썬 인터뷰 p.387 
    - the number of times that the while loop repeats is the depth 
    - for-loop used to operate for all elements in single depth, 
    - at each depth, children of nodes in the same depth or level would be appended to deq, 
    - and after the children of the nodes in the same depth/level has been appended, 
      we can finsh the loop and add one more to the height. 

    - while loop => depth times 
    - for loop => max nodes in a level 

    total runtime = O(depth * max nodes in a level) 
    """

    def maxDepth_iterative(self, root: TreeNode) -> int:
        if not root:
            return 0

        height = 0
        deq = deque([root])

        while deq:
            for _ in range(len(deq)):
                curNode = deq.popleft()

                if curNode.left or curNode.right:
                    if curNode.left:
                        deq.append(curNode.left)
                    if curNode.right:
                        deq.append(curNode.right)

            height += 1

            # print(curNode, deq)

        return height
