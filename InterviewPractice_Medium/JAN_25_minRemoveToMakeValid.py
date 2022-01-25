"""
Mininum to Make Valid Parenthesis 


Approach: 
- use stack 
- loop over s, 
- if (,  append IND to stack 
- else pop from stack (but only if there are elements in the stack; if no el, then append IND

after looping s 
stack will contain unmatched parens 

convert s -> arr for easier removal 
find out the ind of the unmatched paren (ind are saved in stack)
set the ind of arr -> "" 

join the arr and return

"""


class Solution:
    # TC : O(N), where N = len(s)
    def minRemoveToMakeValid(self, s):
        stack = []

        for i in range(len(s)):
            char = s[i]
            if char == "(":
                # stack.append((char, i))
                stack.append(i)  # 현재 인덱스 추가. # ))(())
            elif char == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)

        # after the for loop,
        # only unmatched parens will be left in stack
        print(stack)
        sarr = list(s)

        if stack:
            for el in stack:
                ind = el
                sarr[ind] = ""

        return "".join(sarr)

# if __name__ == "__main__":


s = "lee(t(c)o)de)"
s = "))(("

stn = Solution()
print(stn.minRemoveToMakeValid(s))
