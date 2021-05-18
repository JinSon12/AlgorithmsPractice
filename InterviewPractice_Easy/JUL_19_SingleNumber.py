""" 
		 아이디어: XOR(^)의 성질 이용
		 A ^ 0 = A
		 A ^ A = 0
		 A ^ B ^ A = B
		 -> 중복되는 숫자는 0으로 되어 버리고, 0과 XOR연산을 하면 그대로 나오는것을 이용
		 -> 이 작업은 곱셈처럼 순서가 바뀌어도 상관없다
[출처] 136. Single Number|작성자 worldbiomusic
https://blog.naver.com/ljh3047063/222293595755

"""

# https://leetcode.com/problems/single-number/


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = 0

        for num in nums:
            print(temp ^ num)
            temp ^= num

        return temp


""" 
A bit more about XOR 
output = 6 ^ 3     <-- will Compare the binary versions of 6, 3 which are 110 and 011 and return 101, which is 5 
print(output)

# returns 5. 

"""
