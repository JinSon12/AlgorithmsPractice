# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/submissions/detail/523814657/
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        curr = root
        result = []

        # if len(stack) != then True.
        while(True):

            # until we are at the leftmost node
            if curr is not None:
                stack.append(curr)
                curr = curr.left
                print(curr)
                print(stack)

            elif stack:
                curr = stack.pop()
                print(curr)
                result.append(curr.val)
                curr = curr.right
            else:
                break

        return result
