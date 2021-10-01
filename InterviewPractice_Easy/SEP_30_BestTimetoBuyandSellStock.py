"""
Best Time to Buy and Sell Stock 

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        minVal = prices[0]
        maxDiff = 0 
        
        for el in prices: 
            # if el smaller than top of the stack 
            minVal = min(minVal, el)
            maxDiff = max(maxDiff, el - minVal)
        
        return maxDiff

    def maxProfit_usingStack(self, prices: List[int]) -> int:
        stack = [] 
        minVal = prices[0]
        maxDiff = 0 
        
        for el in prices: 
            # if el smaller than top of the stack 
            if stack: 
                if stack[-1] > el: 
                    stack.pop() 
                else: 
                    maxDiff = max(maxDiff, el - minVal)
            
            minVal = min(minVal, el)
            stack.append(el)
        
        return maxDiff

    def maxProfit_fromBack(self, prices: List[int]) -> int:
        biggest = prices[len(prices)-1]
        profit = 0
        
        for i in range (len(prices)-1, 0, -1):
            if (biggest < prices[i]):
                biggest = prices[i]
            if biggest - prices[i-1] > profit:
                profit = biggest - prices[i-1]
        
        if profit > 0:
            return profit
        else:
            return 0