# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Main Logic: 
if minBound < node < maxBound : VALID 
the value of the leftMinBound and right MinBound : think about it starting from the root. 
- the left child's minBound would not matter as long as it is smaller than the root (upper bound for the child node)
- the right child's minBound would be more important than the maxBound, (b/c maxBound can be +inf)  
    - as long as the minBound is bigger than the root, then node is valid. 

- This logic would ensure that the left child is always smaller than the parent, 
   and the right child is always bigger than the parent (including grandparent)

- 수학적 귀납법과 BST 의 chracteristic 인 strict 한 child and parent's size difference 생각해보기. 
"""


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root.val != None and root.left == None and root.right == None:
            return True
        return self.check_validity(root)

    # using default values (optional values if no parameter has been passed);
    # i.e. check_validity(root, 3, 5) would use 3 as the lower value
    # if check_validity(root), then lower would be -sys.maxsize, vice versa for upper.
    def check_validity(self, node, lower=(-sys.maxsize), upper=(sys.maxsize)):
        if node is None:
            return True

        # for checking the condition:
        # a node must be in between the lower and the upper bound.
        if lower < node.val < upper:
            left = self.check_validity(node.left, lower, node.val)
            right = self.check_validity(node.right, node.val, upper)
            return left and right

        else:
            return False
