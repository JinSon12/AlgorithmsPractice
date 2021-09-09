"""
Lowest Common Ancestor 

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

- parents
# Benefits of using dictionary for this problem: 
# we need dictionary to quickly access node's parents, in O(1), 
# and get data (value) associated with the parents, 
# which is not possible using list (speedwise), or set(cannot store extra data for values)

- p_parents
- use set, 
- because at this point, we only want the parents (no extra data associated with parents, but only parents)
- furthermore, we want to access the parents quickly (in amortized O(1), rather than O(n) with list)
- hence, we go with set. 

"""

from collections import deque


class Solution:
    def lowestCommonAncestor_BFS(self, root, p, q):
        # using BFS,
        # save all the nodes' parents into parents dictionary
        q = deque([root])
        parents = {root: None}

        while q:
            node = q.popleft()

            if node.left:
                q.append(node.left)
                parents[node.left] = node

            if node.right:
                q.append(node.right)
                parents[node.right] = node

        # we create a set of the parents of the node p or q (this case, we go with p.)
        # to store the parents of p.
        p_parents = set({})

        # setting condition to while p:
        # would not advance further when we are at the root node.
        while p:
            p_parents.add(parents[p])       # add the parent of p to p_parents
            p = parents[p]                  # now, p becomes the parent of p,
            # and repeat the process of saving the parent, and moving up the tree

        # termination condition: when q is in the p_parents
        # this means that there is a common parent between p and q.
        # we don't want to go further, because we want to find the LCA
        while q not in p_parents:
            q = parents[q]

        # we return q. (not p, because p will point to the root)
        return q

    def lowestCommonAncestor_recursive(self, root, p, q):
        # termination condition
        # if p or q is found, return the root.
        if root == q or root == q:
            return root

        left = right = None
        if root.left:
            left = self.lowestCommonAncestor_recursive(root.left, p, q)

        if root.right:
            right = self.lowestCommonAncestor_recursive(root.right, p, q)

        # if both left and right returned nodes,
        # 어떠한 노드를 기준으로 그 양 옆의 (left, right) 노드가 p,q 라면, 지금 현재의 노드가 LCA
        # then we want to return the root as the LCA
        if left and right:
            return root

        else:
            # return whichever that has returned a node (which would be either p or q)
            return left or right

    def lowestCommonAncestor_fasterRecursive(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root

        if root.val == p.val or root.val == q.val:
            return root

        lres = self.lowestCommonAncestor(root.left, p, q)
        rres = self.lowestCommonAncestor(root.right, p, q)

        if lres and rres:
            return root

        return lres if lres else rres
