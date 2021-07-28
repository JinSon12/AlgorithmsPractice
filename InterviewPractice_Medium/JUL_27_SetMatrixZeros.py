class Solution:

    # 1st try, 96.67%
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        place = []
        replacement = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    place.append((i, j))
                    # matrix[i] = replacement

        # print(place)

        for i in range(len(place)):
            row, col = place[i][0], place[i][1]
            matrix[row] = replacement
            for j in range(len(matrix)):
                matrix[j][col] = 0

        # print(matrix)
