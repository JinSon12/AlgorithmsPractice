# 1342. Number of Steps to Reduce a Number to Zero

class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0

        # while condition is true:
        while(num != 0):
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1
            counter += 1

        return counter
