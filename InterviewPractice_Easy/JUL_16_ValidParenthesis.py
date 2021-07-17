# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_d = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for brace in s:
            if brace not in p_d:
                stack.append(brace)

            # 하나라도 맞지 않으면 valid 하지 않다.
            # empty stack would have len 0 => False.
            # not stack would return True if empty: https://docs.python.org/3/library/stdtypes.html#truth-value-testing
            elif not stack or p_d[brace] != stack.pop():
                return False

        # 스택 안에 있는 것이 다 확인되었다.
        # edge 케이스 확인 하기. 항상.
        return len(stack) == 0
