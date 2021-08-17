class Solution:
    board = [[]]

    def isValid33(self):
        uniqNum = set()
        x = y = 0

        while x <= 6 and y <= 6:
            for i in range(x, x+3):
                for j in range(y, y+3):
                    num = self.board[i][j]
                    if num != ".":
                        # print(num, i,j, uniqNum)
                        if num in uniqNum:
                            return False
                        else:
                            uniqNum.add(num)
            uniqNum = set()

            x += 3

            if x == 9:
                y += 3
                x = 0

        return True

    def checkRow(self):
        uniqRow = set()

        for i in range(9):
            for j in range(9):
                num = self.board[i][j]
                if num != ".":
                    if num in uniqRow:
                        # print(num, "false")
                        return False
                    else:
                        uniqRow.add(num)
            uniqRow = set()

        return True

    def checkCol(self):
        uniqRow = set()

        for i in range(9):
            for j in range(9):
                num = self.board[j][i]
                if num != ".":
                    if num in uniqRow:
                        return False
                    else:
                        uniqRow.add(num)
            uniqRow = set()
        return True

    def isValidSudoku_v1(self, board: List[List[str]]) -> bool:
        self.board = board

        if self.checkRow() and self.checkCol() and self.isValid33():

            return True
        else:
            return False

    # ==============
    # fastest Version

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)]
        columnSets = [set() for _ in range(9)]
        boxSets = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in columnSets[i]:
                        return False
                    else:
                        columnSets[i].add(board[i][j])

                    if board[i][j] in rowSets[j]:
                        return False
                    else:
                        rowSets[j].add(board[i][j])

                    if board[i][j] in boxSets[i//3][j//3]:
                        return False
                    else:
                        boxSets[i//3][j//3].add(board[i][j])
        return True

    # least memory
    def isValidSudoku_memoryEfficient(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    cur = board[i][j]
                    if (i, cur) in seen or (cur, j) in seen or (i//3, j//3, cur) in seen:
                        return False
                    seen.add((i, cur))
                    seen.add((cur, j))
                    seen.add((i//3, j//3, cur))
        return True
