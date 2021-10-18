"""
Valid Perfect Square 

https://leetcode.com/problems/valid-perfect-square/


Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

pl, mid, p2 의 값을 사용하여서 
mid ** 2 가 원래 수이면 정답. 
mid ** 2 < 원래 수이면, pl += 1 
mid ** 2 > 원래 수, pr -= 1 

"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        p1 = 2
        p2 = num

        while p2 >= p1:
            mid = (p1 + p2) // 2
            sq = mid ** 2
            print(mid, p2, p1)

            if sq == num:
                return True
            elif sq < num:
                p1 = mid + 1
            else:
                p2 = mid - 1

        return False
