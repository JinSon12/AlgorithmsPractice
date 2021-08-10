# https://leetcode.com/problems/power-of-two/

"""
231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2^x.


- recursive 
- bitwise 
- Iterative 
하게 풀 수 있다. 

"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        if n % 2 != 0 or n == 0:
            return False

        return self.isPowerOfTwo(n//2)

    """
    bitwise solution 
    https://leetcode.com/problems/power-of-two/discuss/676737/Python-Oneliner-O(1)-bit-manipulation-trick-explained
    
    이진법으로 바꾸어서 생각해보기. 
    1 = 1
    2 = 10 (2 의 자리에 1, 그외는 0 )
    3 = 011 
    4 = 100 (2^2 의 자리에 1, 그 외는 0)
    7 = 0111 (2^2 의 자리에 1, 2 의 자리에 1, 1의 자리에 1)
    8 = 1000 (2^3 의 자리에 1, 그외는 0)

    12 => 1100 

    7,8 을 예시로 들었을때, 
    - Bitwise AND (&) 를 사용하면, 두 자리에 같은 수가 있을때만 1이다. 
    - 즉 7 = 0111 
        8 = 1000 으로 한 자리에 똑같은 수가 없다. 
      
      7 & 8 은 결과적으로 0이 된다. 
    
    - 2진법은 2의 배수일때 새로운 자리가 추가된다. 3,4 비교. 11은 두자리이지만, 100 (4) 는 3자리수이다. 
    - 즉, 2의 배수 직전의 수는 항상 꽉 찬 1이고, 2의 배수는 그 직전의 자리수에 하나 더 하고, 새로운 자리에 1, 그 직전의 수의 자리에는 모두 0이 된다. 
    """

    def isPowerOfTwo_bitwise(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0 
