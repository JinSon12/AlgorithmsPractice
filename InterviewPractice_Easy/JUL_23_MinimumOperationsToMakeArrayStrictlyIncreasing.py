class Solution:
    """
    very similar to programmers joystick q. (but easier)
    """

    def minOperations(self, nums: List[int]) -> int:
        counter = 0

        for i in range(1, len(nums)):
            oldi = nums[i]

            if nums[i-1] >= nums[i]:
                nums[i] = nums[i-1] + 1
                counter += nums[i] - oldi

        return counter

    # Faster solution than the first solution
    """ 
    Insight: 
    - always think about the output. 
    - we don't want to make unneccessary changes to the original array unless told so. (takes extra time)

    """

    def minOperations_V2(self, nums: List[int]) -> int:
        counter = 0
        # here the value of oldi changes, but not the original array nums.
        oldi = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= oldi:
                oldi += 1
                counter += oldi - nums[i]

            else:
                oldi = nums[i]

        return counter
