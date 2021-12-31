
""" 
start time: 10:12PM EST 

Permutations
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

order does matter. 
			X 
	1 			2 
2  3 		1		3	
3  2 		3		1 


Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]


Example 4: 
inp = [] 
output = [] 

output = [] 

def permutation(nums): # [ 0, 1 ]
	if not nums: 
  	return [] 
  
  if len(nums) == 1: 
  	return nums
    
  DFS(ind, pathSoFar): 
    # termination condition 
    if len(pathSoFar) == len(nums): 
      output.append(pathSoFar[:])
      return

    # 2nd termination condition 
    if ind > len(nums) - 1:
      return 



    for i in range(ind, len(nums)): 
      DFS(i + 1, pathSoFar + [nums[i]])
      	dfs(0+1, [0])
        	dfs(1 + 1 -> 2, [0, 1])
          	dfs(2 + 1 -> 3, ) -> append 
          dfs(2 + 1 -> 3, [0, 3] )
      
DFS(0, [])

class Solution:
    def permute(self, nums):
        """
: type nums: List[int]
: rtype: List[List[int]]
"""
        def backtrack(first = 0):
            # if all integers are used up
            if first == n:  
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output

https://www.youtube.com/watch?v=s7AvT7cGdSo 

https://leetcode.com/problems/permutations/solution/

	

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

"""
