"""
Lowest Common Ancestor of Binary Search Tree

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

- Think about the structure of the BST (root.left < root < root.right)

"""


class Solution:
    def lowestCommonAncestor_v1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        # 속도에 있어서 중요한 부분이다.
        # BST 의 성질을 잘 이용해보면 필요하지 않는 recursion을 피할 수 있다.
        if p.val < root.val < q.val or q.val < root.val < p.val:
            return root

        left = right = None
        if p.val > root.val or q.val > root.val:
            left = self.lowestCommonAncestor(root.right, p, q)
        if p.val < root.val or q.val < root.val:
            right = self.lowestCommonAncestor(root.left, p, q)

        # print(left, right)
        if left and right:
            return root
        else:
            return left or right

    def lowestCommonAncestor_fastest(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root
        return root

    def lowestCommonAncestor_simplified_short(self, root, p, q):
        a, b = sorted([p.val, q.val])
        while not a <= root.val <= b:
            root = (root.left, root.right)[a > root.val]
        return root

    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root
