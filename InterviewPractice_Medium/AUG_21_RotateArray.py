"""
https://leetcode.com/problems/rotate-array/

189. Rotate Array 

while two pointer solution 복습하기 
"""


class Solution:
    # O(n) time, space: O(n)
    def rotate_v1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = nums[:]

        for i in range(len(nums)):
            num = res[i]

            new = i + k
            if i + k > len(nums) - 1:
                new = new % (len(nums))

            # print(new)
            nums[new] = num

        return nums

    # time O(n), space: O(n), faster than rotate_v1
    """
    A little important thing to be cautious:

    nums[:] = nums[n-k:] + nums[:n-k] 
    can't be written as:

    nums = nums[n-k:] + nums[:n-k]
    on the OJ.

    The previous one can truly change the value of old nums, 
    but the following one just changes its reference to a new nums not the value of old nums.
        
    """
    # fastest solution (180~200ms)
    # 99% (196ms)

    def rotate_v2_listSlicing(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    """
    Using pointer (cur and next) and a variable to save the next value to place 
    
    230~ms 
    """

    def rotate_v3_pointerJumping(self, nums: List[int], k: int) -> None:
        start = 0
        count = 0
        cur = 0

        # repeats for len(nums) times, each time there is a jump, count increased by 1.
        while count < len(nums):
            cur = start
            prev = nums[start]

            # inner loop does jumping from index i, i + k .. until index i is met again.
            while True:
                nxt = (cur + k) % len(nums)
                # save the next place's value in a temp, and update the prev value with the next place's value
                t = nums[nxt]
                nums[nxt] = prev
                prev = t

                cur = nxt
                count += 1

                if cur == start:  # don't want to go in an infinite loop.
                    break

            start += 1
