class Solution:
    def nextGreaterElement(self, n: int) -> int:
        numStr = list(str(n))

        firstSmallDig = None

        # first loop to find a number from the right that is smaller than the number
        # on its right (어떤 자리의 수 보다 오른쪽으로 더 큰 수가 있는 곳의 자리 찾기)
        # 왜냐: 바꾼 숫자가 커야하니까.
        for ind in range(len(numStr)-1, -1, -1):
            if ind > 0 and numStr[ind-1] < numStr[ind]:
                firstSmallDig = ind-1
                # print("firstSmallDig", firstSmallDig)
                break

        if firstSmallDig == None:
            return -1

        # finding the next smallest digit from the
        # numbers to the right after we find the firstSmallDig
        nextSmallInd = firstSmallDig + 1
        for ind in range(firstSmallDig + 1, len(numStr)):
            if ind+1 < len(numStr) and numStr[ind+1] < numStr[nextSmallInd]:
                nextSmallInd = ind+1
                # print(numStr[nextSmallInd])

        numStr[firstSmallDig], numStr[nextSmallInd] = numStr[nextSmallInd], numStr[firstSmallDig]

        # print(numStr)

        # sorting the elements of the digits after the first small digit ind.
        numStr[firstSmallDig+1:] = sorted(numStr[firstSmallDig+1:])

        # print(numStr)

        return("".join(numStr))
