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

    # 140ms,
    # instead of modifying the array,
    # calculation done mathematically.
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        pos = 0
        count = 0
        while pos < len(flowerbed):
            if not flowerbed[pos]:
                if pos == len(flowerbed)-1 or flowerbed[pos+1] == 0:
                    count += 1
                    pos += 2
                else:
                    pos += 3
            else:
                pos += 2

            if count == n:
                return True
        return False
