class Solution:
    def maximum69Number(self, num: int) -> int:
        numList = [int(x) for x in str(num)]

        for i in range(len(numList)):
            if numList[i] == 6:
                numList[i] = 9
                break

        numStr = [str(x) for x in numList]

        return(int("".join(numStr)))

    def maximum69NumberUsingEnumerate(self, num: int) -> int:
        digits = list(str(num))
        for index, digit in enumerate(digits):
            if digit == '6':
                digits[index] = '9'
                break
        return int(''.join(digits))
