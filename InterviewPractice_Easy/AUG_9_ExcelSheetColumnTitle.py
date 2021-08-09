# https://leetcode.com/problems/excel-sheet-column-title/

from typing import Collection

"""
168. Excel Sheet Column Title


"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabets = []

        # A의 번호부터 시작해서 Z 의 번호까지 추가.
        for i in range(ord("A"), ord("Z")+1):
            alphabets.append(chr(i))

        res = Collection.deque()

        while columnNumber > 0:
            # print(divmod(columnNumber, 26), columnNumber)
            res.appendleft(alphabets[columnNumber % 26 - 1])
            # print(res)

            # https://leetcode.com/problems/excel-sheet-column-title/discuss/441430/Detailed-Explanation-Here's-why-we-need-n-at-first-of-every-loop-(JavaPythonC%2B%2B)
            columnNumber = (columnNumber - 1) // 26     # -1 을 해 줘야 하는 이유.

        return "".join(res)
