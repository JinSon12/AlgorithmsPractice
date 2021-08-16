# https://leetcode.com/problems/next-permutation/

"""
Key Insight: 

- use Next Lexicographical Permutation Algorithm 

0) use left and right pointers. 
1) using left pointer, start traversing from the end - 1 to index 0 
2) find if nums[left] <= nums[left + 1]
3) using the right pointer, start traversing from the end to index 0 
4) find if nums[right] >= nums[left] 

4-1) if right, left == 0, then we are at the beginning of the array
4-2) sort all the elements ascendingly. 

5) swap elements at left and right of nums 

6) sort ascending from nums[left + 1] and till the end. 


복습 요. 

"""


class Solution:
    # 44ms
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # runtime: O(2n)

        left = len(nums) - 2    # for comparing left and left + 1
        right = left + 1

        while nums[left] >= nums[left + 1]:
            if left <= 0:
                # left = 0
                break
            else:
                left -= 1

        while nums[right] <= nums[left] and right >= 0:
            if right <= 0:
                break
            else:
                right -= 1

        nums[left], nums[right] = nums[right], nums[left]

        # print(nums, left, right)

        if left == 0 and right == 0:
            nums.sort()

        # 이때, nums[left + 1 :] 까지의 원소는 descendingly sorted 되어 있다.
        # 따라서 ascending sort 하려면 중간 기점으로 swap 해주면 된다.
        else:
            left += 1
            right = len(nums) - 1

            while left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

    # 16ms, faster and more concise.
    def nextPermutation_fastest(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2

        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = len(nums)-1

            while j > i and nums[i] >= nums[j]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        self.reverse(nums, i+1)

    def reverse(self, nums, start):
        i = start
        j = len(nums)-1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
