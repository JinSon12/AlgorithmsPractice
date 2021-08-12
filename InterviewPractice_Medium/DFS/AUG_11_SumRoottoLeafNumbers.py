class Solution:
    res = 0

    # 28ms ~ 32ms, 14 MB
    # recursively DFS
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, numSoFar):
            if not node.left and not node.right:
                self.res += int((numSoFar) + str(node.val))
                return

            # print(node.val)
            if node.left:
                dfs(node.left, numSoFar + str(node.val))

            if node.right:
                dfs(node.right, numSoFar + str(node.val))

        dfs(root, "0")
        return self.res

    # 28 ~ 32ms, 14.4 MB
    # because of the removed conditional recursion (if ... dfs)
    # uses more memory (unncessary recursion)
    def sumNumbers_nonConditional_recursion(self, root: Optional[TreeNode]) -> int:
        def dfs(node, numSoFar):
            if not node:
                return

            if not node.left and not node.right:
                self.res += int((numSoFar) + str(node.val))
                return

            dfs(node.left, numSoFar + str(node.val))
            dfs(node.right, numSoFar + str(node.val))

        dfs(root, "0")
        return self.res

    def sumNumbers_moreConcise_recursion(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, num):
        if not root.left and not root.right:
            # 숫자 덧셈하기 항상 이렇게...
            self.res += (10*num + root.val)
        if root.left:
            self.dfs(root.left, 10*num+root.val)
        if root.right:
            self.dfs(root.right, 10*num+root.val)
