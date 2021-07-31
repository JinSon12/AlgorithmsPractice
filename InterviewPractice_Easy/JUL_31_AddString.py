class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        diff = abs(len(num1) - len(num2))
        shorter = min(len(num1), len(num2))
        n1 = ""

        if shorter == len(num1):
            n1 = [0] * diff + list(num1)
            n2 = num2
        elif shorter == len(num2):
            n1 = [0] * diff + list(num2)
            n2 = num1

        point = len(n2) - 1
        place = 1
        res = 0
        carry = 0
        while point >= 0:
            addition = int(n1[point]) + int(n2[point])
            res += ((addition + carry) % 10) * place
            carry = (addition + carry) // 10
            place *= 10
            point -= 1

        if carry > 0:
            res += carry * place

        return str(res)
