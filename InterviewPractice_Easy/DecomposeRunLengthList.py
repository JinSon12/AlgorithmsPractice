# https://leetcode.com/problems/decompress-run-length-encoded-list/

# https://www.kite.com/python/answers/how-to-specify-the-increment-of-a-for-loop-in-python


# nested for loop -> O(n*m)
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            print(i)
            for j in range(nums[i]):
                res.append(nums[i+1])

        return res


def decompressRLElist2(nums: List[int]) -> List[int]:
    lst = []
    num = ''

    for i in range(len(nums) - 1):
        if i % 2 == 0:
            num = nums[i] * (str(nums[i + 1]) + ',')
            print(num)
            num = num[:-1]
            print(num)
            lst.append(num)

    print(lst)


decompressRLElist2([1, 1, 2, 3])


def decompressRLElist3(nums: List[int]) -> List[int]:
    res = []
    for i in range(0, len(nums), 2):
        # res += [nums[i+1]]*nums[i]
        res.extend([nums[i+1]] * nums[i])

    return res
