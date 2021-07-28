# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

""" 
REVIEW NEEDED!!! 

KEY Insight: 
- Inorder traversal, Recursion 
- Go to the leftmost leaf node, and start calculating. 
- Inorder Traversal would be from L -> Self -> R

Key Points to think about: 
- No need to use abs(), as traversing using in-order, we can leverage that to yield always positive values 
- (i.e. curNode - prevNode; the prev nodes would always have smaller values due to the characterstics of the inorder traversal)


1st try: Fast solution, 95.97%, 48ms 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from InterviewPractice_Easy.Tree.TreeNode import TreeNode


class Solution:

    # want to set the abs value as the max (so that we can decrease in the future)
    min_val = sys.maxsize

    # -sys.maxsize, as root.val - sys.maxsize would return very small #
    # and result in incorrect min_val.
    prev_node = -sys.maxsize

    def getMinimumDifference(self, root: TreeNode) -> int:

        # using in-order traversal:
        if root.left:
            self.getMinimumDifference(root.left)

        self.min_val = min(self.min_val, root.val - self.prev_node)
        self.prev_node = root.val

        if root.right:
            self.getMinimumDifference(root.right)

        return self.min_val

    # 32ms
    def getMinimumDifference_Fastest(self, root: TreeNode) -> int:
        lst = []

        # recursive dfs (inorder) function
        def helper(root: TreeNode):
            if not root:
                return
            helper(root.left)
            lst.append(root.val)
            helper(root.right)

        ans = float('inf')
        helper(root)

        if len(lst) == 1:
            return 0

        for i in range(len(lst) - 1):
            ans = min(ans, lst[i + 1] - lst[i])

        return ans
