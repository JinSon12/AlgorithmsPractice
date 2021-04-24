
class Solution:
  # faster solution 
  def twoSum(self, nums: List[int], target: int) -> List[int]:
        newDict = {}
        needValue = 0 
        
        for i in range(len(nums)) : 
            needValue = target - nums[i] 
            if (newDict.get(needValue)!= None):
                return [newDict.get(needValue), i]
            else : 
                newDict[nums[i]] = i
        return None 
            

# solution with low memory usage. 
  def twoSum1(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in sorted(nums):
            if i in nums and target-i in nums:
                if i == target -i and nums.count(i) >= 2:
                    ans.append(nums.index(i))
                    ans.append(nums.index(i,nums.index(i)+1))
                    return ans
                elif i != target - i:
                    ans.append(nums.index(i))
                    ans.append(nums.index(target-i))
                    return ans
        