# https://leetcode.com/problems/can-place-flowers/

"""
605. Can Place Flowers

- Greedy 

"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        num_total_flow, r = divmod(len(flowerbed), 2)

        if r != 0:
            num_total_flow += 1

        for i in flowerbed:
            if i == 1:
                num_total_flow -= 1

        if num_total_flow >= n:
            return True

    # 164ms, 72%
    # checking front and back, of the position i and position i has value of 0 (no flower) greedily.
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, v in enumerate(flowerbed):
            if v == 0:
                if i == 0 or flowerbed[i - 1] == 0:
                    if i == len(flowerbed) - 1 or flowerbed[i+1] == 0:
                        n -= 1
                        flowerbed[i] = 1

        return n <= 0
