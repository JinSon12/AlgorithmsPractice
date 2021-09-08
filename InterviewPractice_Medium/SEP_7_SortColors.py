"""
Sort Colors 

https://leetcode.com/problems/sort-colors/submissions/

Key Insight: 
- 두번째 for loop 에서 어떻게 하면 nested for loop 사용하지 않고 원소를 추가할까 생각. 
- val = count[ind]
- val 횟수만큼 ind 값을 num에 overwrite 한다. 
- i 값과 count 와 val 값을 생각하면서 ind 값을 변경한다. 

"""


class Solution:
    def sortColors_v1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0 for _ in range(3)]

        for n in nums:
            count[n] += 1

        # print(count)

        ind = 0
        val = count[ind]
        for i in range(len(nums)):
            if val > i:                 # val의 횟수만큼 0부터 val 까지 반복해서 추가하기.
                nums[i] = ind
            else:                       # i 이 val 보다 같거나 크다면,
                ind += 1
                if count[ind] == 0:
                    while count[ind] == 0:
                        ind += 1
                        val += count[ind]
                        # print(ind)
                else:
                    val += count[ind]

                nums[i] = ind

        # print(nums)

    # more concise!!!
    # KISS!! Keep it Simple
    def sortColors_v2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0 for _ in range(3)]

        for n in nums:        # for loop 을 돌면서 원소의 갯수를 count[원소] 에 저장한다.
            count[n] += 1

        for i in range(len(nums)):
            if i < count[0]:
                nums[i] = 0
            elif i < count[0] + count[1]:
                nums[i] = 1
            else:
                nums[i] = 2
