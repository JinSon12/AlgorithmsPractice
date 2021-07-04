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
            if numStr[ind] < numStr[nextSmallInd] and numStr[firstSmallDig] < numStr[ind]:
                nextSmallInd = ind
                # print(numStr[nextSmallInd])

        numStr[firstSmallDig], numStr[nextSmallInd] = numStr[nextSmallInd], numStr[firstSmallDig]

        # print(numStr)

        # sorting the elements of the digits after the first small digit ind.
        numStr[firstSmallDig+1:] = sorted(numStr[firstSmallDig+1:])

        # print(numStr)
        if int("".join(numStr)) > 2147483647:
            return -1
        else:
            return "".join(numStr)

    def nextGreaterElementV2(self, n: int) -> int:
        num = list(str(n))
        ret = -1
        for i in range(len(num)-1, 0, -1):
            if num[i] > num[i-1]:
                for j in range(len(num)-1, i-1, -1):
                    if num[j] > num[i-1]:
                        num[j], num[i-1] = num[i-1], num[j]
                        break
                ret = int("".join(num[:i]+num[-1:i-1:-1]))
                if ret > (2**31 - 1):
                    ret = -1
                return ret
        return ret

    def nextGreaterElementV3(self, n: int) -> int:
        if n <= 11:
            return -1
        s = str(n)
        ln = len(s)
        fg = 0
        ind1, ind2 = -1, -1
        for i in range(ln-1, 0, -1):
            m = int(s[i])
            for j in range(i-1, -1, -1):
                if int(s[j]) < m:
                    if j > ind1:
                        ind1 = j
                        ind2 = i
                        break
        if ind1 == -1:
            return -1
        ans = list(s)
        ans[ind1], ans[ind2] = ans[ind2], ans[ind1]
        # sorting the right half after ind1 because that oart should be in accending order for lowest
        ans[ind1+1:] = sorted(ans[ind1+1:])
        st = "".join(ans)
        an = int(st)
        if an > (2**31-1):
            return -1
        return an
