# https://leetcode.com/problems/palindrome-number/

"""
List Slicing : 문자열 조작할때 반드시 이것 사용하기. 

슬라이싱을 이용할 때,
우리가 위치를 지정해주면 해당 위치를 가진 배열의 포인터를 얻게 된다.
이를 통해 연결된 객체를 찾아 실제 값을 찾아내는 것이다.
 
이 과정은 속도가 굉장히 빨라서 문자열을 조작할 때면
슬라이싱을 사용하는 것을 권장한다.

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        res = self.v_3(x)

        # compare the numbers and return result
        if res == x:
            return True

    def v_1(self, x):
        stack = []
        divisor = 10
        res = 0
        original = x

        # O(log10(n)) as we divide the input by 10 for every iteration.
        while(x != 0):
            stack.append(x % divisor)
            x = x // 10

        # using stack, create the number again backwards
        multi = 1
        while (stack):
            res += stack.pop() * multi
            multi *= 10

    def v_2(self, x):
        res = 0
        while (x > 0):
            res = res * 10 + x % 10
            x = x // 10

        return res

    def v_3(self, x):
        strx = str(x)

        if strx == strx[::-1]:
            return int(strx[::-1])
