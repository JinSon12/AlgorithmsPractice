class Solution:

    """ 
    Key Insight: 
    Somewhat Greedy ? 

    - moving 2 places doesn't increase cost 
    - moving 1 place increase cost by one. 

    - in the end, all the elements should move to a single position 
    - it could be from an even position -> odd number position 
    - or it could be the opposite. 

    - whenever we change to even -> odd / odd -> even, 
    - there would be a cost of 1 (times that with the chip count)

    - the total cost of moving to an odd # position would be 1 * # chips in the even position 
    - " but to an even position would be 1 * # of chips in the odd position 
    - compare the two cost, pick the smaller cost. (This would be the greedy part)

    """

    # 99.29% but contains a lot of redundant information
    # 한번 더 생각해보기. Do we really need dictionary?
    # What happens if we don't use the dictionary to store the # of occurences?
    def minCostToMoveChips(self, position: List[int]) -> int:
        chips = {}

        # O(pos)
        for i in position:
            if i not in chips:
                chips[i] = 1
            else:
                chips[i] += 1

        # O(len(pos))
        chips_items = chips.items()

        odd = 0
        even = 0

        # O(len(pos))
        for cid, cnt in chips_items:
            if cid % 2 == 0:
                even += cnt
            else:
                odd += cnt

        return min(odd, even)

    def minCostToMoveChips_moreConcise(self, position: List[int]) -> int:
        odd, even = 0, 0

        # O(len(pos))
        for i in range(len(position)):
            if position[i] % 2 == 0:
                even += 1
            else:
                odd += 1

        return min(odd, even)

    def WRONG(self, position: List[int]) -> int:
        chips = {}

        for i in position:
            if i not in chips:
                chips[i] = 1
            else:
                chips[i] += 1

        # O(len(chips))
        chips_items = chips.items()

        # O(len(chips))
        maxChipId = max(chips_items, key=lambda x: x[1])[0]

        res = 0

        # 요기가 하이라이트.
        """
        Logic: 2칸씩 움직이는 것은 0, 1칸은 1 
        ex) 1, 6 일때, 가야하는 거리는 5. 2칸씩 2번, 1칸씩 한번 움직이면 된다. 총 cost 는 1

        """
        for chip_id, cnt in chips_items:
            if chip_id != maxChipId:
                if abs(chip_id - maxChipId) % 2 != 0:
                    res += 1 * cnt

        return res
