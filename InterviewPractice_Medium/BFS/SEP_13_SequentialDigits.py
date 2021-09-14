"""
Sequential Digits 

"""

from collections import deque
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        numbers = "123456789"
        res = []

        q = deque([[numbers[i], i+1] for i in range(len(numbers)-1)])

        while q:
            path, ind = q.popleft()

            if ind < len(numbers):
                path += numbers[ind]
                intpath = int(path)

                if intpath <= high:
                    if low <= intpath <= high:
                        res.append(intpath)
                    q.append([path, ind + 1])

        return res

    def sequentialDigits_v2(self, low: int, high: int) -> List[int]:
        res = []

        for startingDigit in range(1, 10):  # 1~9 까지의 숫자만 본다.
            num = 0
            dig = startingDigit

            while num <= high and dig <= 9:
                num = num * 10 + dig

                if low <= num <= high:
                    res.append(num)

                dig += 1

        # sorted 전: [1234, 12345, 2345, 3456, 4567, 5678, 6789]
        return sorted(res)


stn = Solution()
print(stn.sequentialDigits_v2(1000, 13000))
