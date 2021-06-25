class Solution:
    def maximum69Number(self, num: int) -> int:
        numList = [int(x) for x in str(num)]

        for i in range(len(numList)):
            if numList[i] == 6:
                numList[i] = 9
                break

        numStr = [str(x) for x in numList]

        return(int("".join(numStr)))
