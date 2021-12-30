"""
Product of Array Except Self 

https://leetcode.com/problems/product-of-array-except-self/

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

1 1 2 6 
  24 

"""


from typing import List


def productExceptSelf_BruteForce(nums: List[int]) -> List[int]:
    res = []

    for i in range(len(nums)):
        tempRes = 1
        for j in range(len(nums)):
            if j != i:
                tempRes *= nums[j]

        res.append(tempRes)

    print(res)
    return res


def productExceptSelf_BruteForce_JAN152022(nums: List[int]) -> List[int]:
    res = []

    for i in range(len(nums)):
        multi = 1
        for j in range(len(nums)):
            if i != j:
                multi *= nums[j]

        res.append(multi)

    return res


""" 
자기 자신을 기준으로 
- 왼쪽시작 숫자에서 에서 자기자신 전의 (자기 자신을 제외한) 숫자까지의 총 곱셈을 구한다. 
- 오른쪽 끝 숫자에서 자기 자신 (자기 자신을 제외한) 앞까지의 숫자까지의 총 누적곱을 구해서 저장한다. 
- 현 


"""


def productExceptSelf_multiplication_JAN152022(nums: List[int]) -> List[int]:
    multiFromLeft = [1] * len(nums)
    multiFromRight = [1] * len(nums)
    res = []

    for i in range(1, len(nums)):
        multiFromLeft[i] = multiFromLeft[i-1] * nums[i-1]

    for j in range(len(nums)-2, -1, -1):
        multiFromRight[j] = multiFromRight[j+1] * nums[j+1]

    print(multiFromLeft, multiFromRight)
    for i in range(len(multiFromLeft)):
        res.append(multiFromLeft[i] * multiFromRight[i])

    return res


productExceptSelf_BruteForce([-1, 1, 0, -3, 3])
