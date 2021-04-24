# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        maxA = heights[0]
        cumA = maxA
        minH = maxA

        dist = 1

        for i in range(1, len(heights)):
            minH = min(minH, heights[i])
            cumA = ((dist + 1) * minH)
            print(cumA, "i", heights[i])
            if(cumA < heights[i]):
                cumA = heights[i]
                minH = heights[i]
                dist = 0
            if cumA == heights[i]:
                if i < len(heights)-1 and heights[i+1] == heights[i]:
                    cumA = heights[i]
                    minH = heights[i]
                    dist = 0
            if maxA < cumA:
                maxA = cumA
            dist += 1

        return maxA
