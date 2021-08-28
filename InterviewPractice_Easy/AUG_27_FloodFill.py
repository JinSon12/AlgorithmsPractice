"""
https://leetcode.com/problems/flood-fill/

Flood Fill 

DFS - color the given numbers and the connected neighbors to the new color
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            temp = image[r][c]
            image[r][c] = -1

            for x, y in dirs:
                newx = r + x
                newy = c + y

                # if not the same color, do not visit.
                if 0 <= newx < len(image) and 0 <= newy < len(image[0]) and image[newx][newy] == temp:
                    dfs(newx, newy)

            image[r][c] = newColor

        dfs(sr, sc)

        return image
