class Solution:
    """
    constraints: 
    length : len(nums) > 0 
    range of values in nums array : positive int. 

    key insight: 
    - two adj. houses, -> invalid case. 

    - dp question 
        - max(previous house (i-2) + case when you rob the current house, previous house (i-1))
    
        - bc 
        - len(nums) == 0, 0 
        - len(nums) == 1, nums[0]
    """
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        
        elif len(nums) == 1: 
            return nums[0]
        
        dp = [0] * len(nums) # 3 까지만 저장해도 된다 ! 생각해보기 .
        # prevNotRob
        # prevRob
        dp[0] = nums[0] 
        dp[1] = max(nums[0], nums[1])
        
        # cases after 2 
        for i in range(2, len(nums)): 
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            # dp[i] = max(notrob+ nums[i], rob)
            # curren
            # int currNotRob=max(prevNotRob,prevRob);
            # int currRob=prevNotRob+nums[i];
            # prevNotRob=currNotRob;
            # prevRob=currRob;
        return dp[len(nums)-1]

# time : O(N)
# space : O(N)
# simulation 돌리기. 