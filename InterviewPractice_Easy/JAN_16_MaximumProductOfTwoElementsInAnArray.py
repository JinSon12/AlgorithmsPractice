"""
1464. Maximum Product of Two Elements in an Array

https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/


Goal 
- find the maximum product of two elements in the given array 

- Heap in Python 
  - Binary heap, 
  - O(log n) push, O(log n) pop 

Approach 1 - Sorting -> O(n log n) -> 
- sort the given array 
- select the top 2 elements from the sorted array 
- do a subtraction on both elements and multiply with each other 
- return the final result. 

Approach 2 - Heap -> O(n log n), SC : O(n)
adv - better avg performance on insertions compared to using a sorted array 
    - worst case insertion changes from O(N) -> O(log N) due to tree 
    - 즉, sorting 된 상태를 유지하면서 계속 원소를 추가, 제거를 해야 할 때. 

- use maxHeap 
- select top 2 elements from the maxHeap 
- do a -1 on each of the 2 elements 
- multiply the 2 elements 
- return the res 

Approach 3 - using max -> O(n)
- use maxi, secondMax 
- if el > max => secondMax = max, and max = el 
- else if el > secondMax => secondMax = el 
- return the multiplication result of maxi - 1 and secondMax - 1 

"""
import heapq


class Solution:
    def maxProduct_sorting(nums):
        # reverse sort 하려면, sort(reverse=True)
        nums.sort()
        lastEl = len(nums) - 1
        # alternatively can use nums[-1], nums[-2]

        return (nums[lastEl] - 1) * (nums[lastEl - 1] - 1)

    """
    implementing maxHeap 

    import heapq

    nums = [4, 1, 7, 3, 8, 5]
    heap = []

    for num in nums:
      heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

    while heap:
      print(heapq.heappop(heap)[1])  # index 1
    
    """
    def maxProduct_heap(nums):
        # maxHeap - element conversion
        for i in range(nums):
            nums[i] *= -1

        heapq.heapify(nums)
        largest = heapq.heappop(nums) * -1
        secondLargest = heapq.heappop(nums) * -1

        return (largest - 1) * (secondLargest - 1)

    def maxProduct_linear(nums):
        maxi = -1
        secondMax = -1

        for el in nums:
            if el > maxi:
                secondMax = maxi
                maxi = el
            elif el > secondMax:
                secondMax = el

        return (maxi - 1) * (secondMax - 1)

    # using heapq.nlargest
    def maxProduct_heap_v2(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        lst = heapq.nlargest(2, nums)
        return (lst[0]-1)*(lst[1]-1)

    # using list comprehension to construct maxHeap
    def maxProduct(self, nums: List[int]) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        max1 = heapq.heappop(max_heap)
        max2 = heapq.heappop(max_heap)

        return (abs(max1)-1) * (abs(max2)-1)
