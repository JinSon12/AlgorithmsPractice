class Solution:
    """
    Key Insght:
    - using stack, when we see (, add to stack, when we see ), pop from stack.

    - HOWEVER! 
    - The requirement says that parenthesis are matched, so there is no single parenthesis floating alone 
    - Alternative way of keeping track of the depth of the parenthesis? 

    """

    # O(n) solution,
    # 28 ~ 32ms
    def maxDepth(self, s: str) -> int:
        stack = [0]
        res = 0

        for i in s:
            if i == "(":
                depth = stack[-1]
                stack.append(i)
                stack.append(depth+1)

            elif i == ")":
                res = max(res, stack.pop())
                stack.pop()

        return res

    """
    - The solution doesn't use stack. 
    - Instead, uses curDepth to keep track of the current depth ("(" -> add 1 depth, ")" -> remove 1 depth) 
    - res is going to take the max of the curDepth when we add to the curDepth 
    - Again, no need to worry about matching the parenthesis. 
    """
    # O(n) solution,
    # 16 ~ 32ms, 100% ~ 65%

    def maxDepth_fastest(self, s: str) -> int:
        curDepth = 0
        res = 0

        for i in s:
            if i == "(":
                curDepth = curDepth+1
                res = max(curDepth, res)

            elif i == ")":
                curDepth -= 1

        return res
