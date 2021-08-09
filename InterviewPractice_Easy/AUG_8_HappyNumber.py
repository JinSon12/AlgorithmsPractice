# https://leetcode.com/problems/happy-number/


"""
202. Happy Number

- Pattern Recognition is the Key!! 
- continue repeating the process and if we see a number that we have already seen, 
- the process for finding happy number for that number would be the same. 

ex) n = 2 
4 -> 16 -> 37 -> .... 42 -> 20 -> 4 (and the loop would become infinite)

- to PREVENT this, we can keep track of the seen (visited) numbers 
- Best DS to use? Set. (Python IN operators for this would be avg O(1), worst O(n), which is faster than using IN on lists. 

- ANOTHER key pattern: 
n = 1, 
1 would always be one. 
so return statement could become more concise to be this: 
return if lastNumber == 1 

"""


class Solution:
    # 36ms, could be faster.
    def isHappy_v1(self, n: int) -> bool:
        visited = set()
        res = n

        while res not in visited:
            visited.add(res)
            s = str(res)
            temp = 0

            for dig in s:
                temp += int(dig) ** 2

            if temp == 1:
                return True

            res = temp

        return False

    # 16ms
    # More concise, faster.
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            # This -> ** is a simple way to denote powers.
            n = sum([int(x) ** 2 for x in str(n)])
        return n == 1

    # 32ms
    # contains important method.
    def isHappy(self, n: int) -> bool:
        def check(num: int) -> int:
            ans = 0
            # ***** keep this handy *****
            # although there might not be a significant time difference between str -> int
            # this is still important.
            while num > 0:
                digit = num % 10
                ans += (digit * digit)
                num = num // 10
            return ans

        seen = set()
        cur = n
        while True:
            n = check(n)
            if n in seen:
                return False

            seen.add(n)

            if n == 1:
                return True
