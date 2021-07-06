class Solution:
    def multiply(sel, num1: str, num2: str) -> str:
        return(str(int(num1) * int(num2)))

    def multiplyV2(self, num1: str, num2: str) -> str:
        carry = 0
        firstTimes = 1
        secTimes = 1
        num = 0

        if len(num1) < len(num2):
            num1, num2 = num2, num1

        for i in range(len(num2)-1, -1, -1):
            for j in range(len(num1)-1, -1, -1):
                # print(num1[j])
                # print("carry", carry)
                tempNum = int(num1[j]) * int(num2[i]) + carry
                carry = 0
                # print("tn", tempNum)

                if tempNum >= 10:
                    carry = tempNum // 10
                    print("carry", carry)
                    tempNum = tempNum % 10
                # print(tempNum, secTimes, firstTimes)
                num += tempNum * secTimes * firstTimes
                # print("num", num)
                secTimes *= 10
                # print("secTimes", secTimes)
            # print("firstTimes after running second loop", secTimes)
            num += secTimes * carry * firstTimes
            carry = 0
            firstTimes *= 10

            # print("num after running second loop", num)
            secTimes = 1

        return(str(num))

    def multiplyV3(self, num1: str, num2: str) -> str:
        res = 0
        carry1 = 1
        dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        for i in num1[-1::-1]:
            carry2 = 1
            for j in num2[-1::-1]:
                res += dict[i]*dict[j]*carry2*carry1
                carry2 *= 10
            carry1 *= 10
        return str(res)
