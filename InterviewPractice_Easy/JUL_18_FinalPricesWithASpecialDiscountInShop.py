# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

""" 
- use Monotinic Stack. 
"""


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = prices[:]

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                prev_ind = stack.pop()
                res[prev_ind] = prices[prev_ind] - prices[i]

            stack.append(i)

        return res
