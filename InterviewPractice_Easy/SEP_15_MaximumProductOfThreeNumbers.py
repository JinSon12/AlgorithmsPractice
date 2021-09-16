"""
https://leetcode.com/problems/maximum-product-of-three-numbers/

Maximum Product of Three Numbers

"""


class Solution:
    def maximumProduct_v1(self, nums: List[int]) -> int:
       # for the case where there is mix of neg. and pos. numbers
        nums.sort()
        neg_nums = []

        # appending to neg_nums
        # O(n)
        for num in nums:
            if num <= 0:
                neg_nums.append(num)

            if len(nums) == 3 and num == 0:
                return 0

        neg_nums.sort(reverse=True)
        # [-1, -2, -3]

        n1 = len(nums) - 1
        res = 1
        # finding the highest number
        if not neg_nums or len(neg_nums) == len(nums):
            for i in range(3):  # o(3)
                res *= nums[n1]
                n1 -= 1
        else:
            # if we use neg numbers, max we can use is 2.
            n2 = len(neg_nums) - 1
            pos_counter = 0

            # compare the values of n1, n2
            n1_largest = 1
            for i in range(3):
                n1_largest *= nums[n1]
                n1 -= 1

            comb_largest = 1
            for i in range(2):
                comb_largest *= neg_nums[n2]
                n2 -= 1

            comb_largest *= nums[len(nums) - 1]

            res = max(n1_largest, comb_largest)

        # decreasing the pointer by 1 to left.
        return res

    # much more concise and faster
    def maximumProduct_v2(self, nums: List[int]) -> int:
       # for the case where there is mix of neg. and pos. numbers
        nums.sort()

        pos = nums[-1] * nums[-2] * nums[-3]
        comb = nums[-1] * nums[0] * nums[1]
        res = max(pos, comb)

        return res
