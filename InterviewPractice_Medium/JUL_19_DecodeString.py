# REVIEW!!!
# https://leetcode.com/problems/decode-string/submissions/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        string = ""
        cur_num = 0

        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)

            elif c == "[":
                stack.append(string)
                stack.append(cur_num)
                cur_num = 0
                string = ""

            elif c == "]" and stack:
                num = stack.pop()
                ps = stack.pop()
                string = ps + (string * num)

            else:
                string += c

        return string

    # Cleanly written sample solution
    def decodeString_V2(self, s: str) -> str:
        curr_string = ""
        stack = []
        k = 0
        for char in s:
            if char.isnumeric():
                k = k * 10 + int(char)
            elif char == "[":
                # NOTICE that I can append 2 things.
                stack.append((curr_string, k))
                k, curr_string = 0, ""
            elif char == "]":
                prev_string, prev_k = stack.pop()
                curr_string = prev_string + prev_k * curr_string
            else:
                curr_string += char
        return curr_string

    # Refactored.
    def decodeString_V3(self, s: str) -> str:
        stack_num = []
        stack_res = []
        res = ""
        char = 0

        while(char < len(s)):
            if s[char].isnumeric():  # char == number,
                numTracker = []      # create temp array to store and parse the number
                while(s[char].isnumeric()):
                    numTracker.append(s[char])
                    strIter += 1

                # append joined number from the numTracker.
                stack_num.append("".join(numTracker))

            elif s[char].isalpha():
                res = res + s[char]
                strIter += 1

            elif s[strIter] == '[':
                stack_res.append(res)  # storing already computed vallue
                res = ""
                strIter += 1

            elif s[strIter] == ']':
                strPop = stack_res.pop()
                cntPop = int(stack_num.pop())
                res = strPop + res * cntPop
                strIter += 1

            else:
                strIter += 1

        return res
