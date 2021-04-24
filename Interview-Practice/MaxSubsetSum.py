def maxSubaray(self, nums: List[int]) -> int: 
  sums: List[int] = [nums[0]]
  for i in range(1, len(nums)): 
    if sums[i-1] > 0: 
      sums.append(nums[i] + sum[i-1])
    else: 
      sums.append(nums[i])
  return 
ans = maxSubaray([])