"""
Sort Colors 

https://leetcode.com/problems/sort-colors/submissions/

Key Insight: 
- 두번째 for loop 에서 어떻게 하면 nested for loop 사용하지 않고 원소를 추가할까 생각. 
- val = count[ind]
- val 횟수만큼 ind 값을 num에 overwrite 한다. 
- i 값과 count 와 val 값을 생각하면서 ind 값을 변경한다.


https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation

https://leetcode.com/problems/sort-colors/discuss/26500/Four-different-solutions

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

    """
    
    This is a dutch partitioning problem. 
    We are classifying the array into four groups: 
    red, white, unclassified, and blue. 
    Initially we group all elements into unclassified. 
    We iterate from the beginning as long as the white pointer is less than the blue pointer.

    If the white pointer is red (nums[white] == 0), 
    we swap with the red pointer and move both white and red pointer forward. 

    If the pointer is white (nums[white] == 1), the element is already in correct place, 
    so we don't have to swap, just move the white pointer forward. 
    
    If the white pointer is blue, we swap with the latest unclassified element.
    """

    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums)-1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
