# https://leetcode.com/problems/rotate-image/submissions/

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mlength = len(matrix)-1

        for i in range(len(matrix[0])):
            newArr = []

            for j in range(mlength, -1, -1):
                newArr.append(matrix[j][i])

            matrix.append(newArr)

        for j in range(mlength, -1, -1):
            matrix.pop(0)

        return matrix

    # v2, fastest

    def transpose(self, matrix):
        n = len(matrix[0])

        for i in range(n):
            for j in range(i, n):

                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reverse(self, matrix):

        n = len(matrix[0])

        for i in range(n):
            for j in range(n//2):

                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

    def rotateV2(self, matrix: List[List[int]]) -> None:

        self.transpose(matrix)
        self.reverse(matrix)

    # V3, using 내장함수.

    def rotate_V3(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


sl = Solution()
sl.rotate()
