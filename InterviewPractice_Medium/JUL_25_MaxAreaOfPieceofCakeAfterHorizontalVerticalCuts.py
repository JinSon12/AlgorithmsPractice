# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

"""
You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

horizontalCuts[i] is the distance from the top of the rectangular cake 
to the ith horizontal cut and similarly, and

verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after 
you cut at each horizontal and vertical position provided 
in the arrays horizontalCuts and verticalCuts. 
Since the answer can be a large number, return this modulo 109 + 7.


Key Insight: 
- Greedy: Which cut has the largest size? Largest cut size would yield the largest cake size. 
- How to calculate each cut? What would be the correct way to get length of piece? 
- start from 0, calculate the distance between each cut points. 
- sort the array so that we can correctly calculate and save max cut length. 

"""


class Solution:

    # 308ms, 81.86%
    # runtime: len(horizontalCuts) = hl + 1 (including the last array appended), and vl = lenVC + 1
    # o(hl log hl) + vl log vl); python sort runtime using TimSort guarantees nlogn
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(h)
        verticalCuts.append(w)

        horizontalCuts.sort()
        verticalCuts.sort()

        hmax = self.findMax(horizontalCuts)
        vmax = self.findMax(verticalCuts)

        return (hmax * vmax) % (10**9 + 7)

    def findMax(self, cuts):
        maxlen = 0
        prev = 0
        for i in cuts:
            length = i - prev
            # print(length)
            maxlen = max(maxlen, length)
            prev = i
        return maxlen

    # 2nd Version, without appending, and using the last number h, w in findMax fn.
    # did not show significant time decrease.
    def maxArea_noAppend(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # horizontalCuts.append(h)
        # verticalCuts.append(w)

        horizontalCuts.sort()
        verticalCuts.sort()

        hmax = self.findMax_noAppend(horizontalCuts, h)
        vmax = self.findMax_noAppend(verticalCuts, w)

        return (hmax * vmax) % (10**9 + 7)

    def findMax_noAppend(self, cuts, end):
        maxlen = 0
        prev = 0
        for i in cuts:
            length = i - prev
            # print(length)
            maxlen = max(maxlen, length)
            prev = i
        maxlen = max(maxlen, end - prev)
        return maxlen

    # https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/discuss/753060/Python-3-%2B-Explanation
    # Discussions forums same logic, but more concise!
    def maxArea_v1(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalStrips = [0] + sorted(horizontalCuts) + [h]
        verticalStrips = [0] + sorted(verticalCuts) + [w]

        maxStripWidth = max([horizontalStrips[i + 1] - horizontalStrips[i]
                             for i in range(len(horizontalStrips) - 1)])
        maxStripHeight = max([verticalStrips[i + 1] - verticalStrips[i]
                              for i in range(len(verticalStrips) - 1)])

        return (maxStripWidth * maxStripHeight) % ((10 ** 9) + 7)

    # https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/discuss/1248641/Python-simple-3-lines-math-solution-explained
    # using Zip function.
    def maxArea_zip(self, h, w, horizontalCuts, verticalCuts):
        H = sorted([0] + horizontalCuts + [h])
        V = sorted([0] + verticalCuts + [w])
        return max(j-i for i, j in zip(H, H[1:])) * max(j-i for i, j in zip(V, V[1:])) % (10**9 + 7)

    # fast solution, using no max, mostly appending to arrays. -> extra space
    def maxArea_fast(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalDiffs = []
        prevHorizontalPosition = 0
        for cut in sorted(horizontalCuts):
            horizontalDiffs.append(cut-prevHorizontalPosition)
            prevHorizontalPosition = cut
        horizontalDiffs.append(h-prevHorizontalPosition)

        verticalDiffs = []
        prevVerticalPosition = 0
        for cut in sorted(verticalCuts):
            verticalDiffs.append(cut-prevVerticalPosition)
            prevVerticalPosition = cut
        verticalDiffs.append(w-prevVerticalPosition)

        return (max(horizontalDiffs)*max(verticalDiffs)) % (10**9+7)
