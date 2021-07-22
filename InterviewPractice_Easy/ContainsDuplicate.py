class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        counter = 0

        for i in range(len(nums)):
            counter += 1
            if counter >= 2:
                return True

            if i+1 < len(nums) and nums[i] != nums[i+1]:
                counter = 0

        return False

    """
    Reflection: 
    Above solution is a general solution that could work telling if an element appears more than k times 
    But the requirement for the problem is much simpler (problem misread)
    - Need to tell if an element appears AT LEAST TWICE. This means 2 or more. 
    - If we use set, which saves information of unique elements, (saves unique chars that have appeared), we can easily find the answer
    - If an element appeared more than once, then the lengh of the array would be greater than the set. 
    - WHILE the below solution is much faster, it would use more space due to the set DS 
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
