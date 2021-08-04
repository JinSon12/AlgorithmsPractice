# https://leetcode.com/problems/pascals-triangle/

"""
118. Pascal's Triangle


Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

"""


class Solution:
    # recursive solution
    # 28 ms ~ 32ms
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        if numRows == 1:
            return [[1]]

        def recurse(elements):
            if len(elements) == numRows:
                return res

            newEl = [1]

            if len(elements) == 1:
                res.append([1, 1])
                recurse([1, 1])

            else:
                for i in range(len(elements)):
                    if i + 1 < len(elements):
                        newEl.append(elements[i] + elements[i+1])
                newEl.append(1)
                res.append(newEl)

                recurse(newEl)

        recurse([1])

        return res

    # iterative solution
    # 28 ms ~ 32ms
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(1, numRows + 1):
            temp = [1] * i

            for j in range(1, i - 1):
                temp[j] = res[-1][j-1] + res[-1][j]

            res.append(temp)

        return res
