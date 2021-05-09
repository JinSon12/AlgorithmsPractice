class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxVal = 0
        for row in accounts:
            curVal = sum(row)
            if curVal > maxVal:
                maxVal = curVal
        return maxVal

    def maximumWealth2(self, accounts: List[List[int]]) -> int:
        return max([sum(i) for i in accounts])
