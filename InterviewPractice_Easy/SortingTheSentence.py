# https://leetcode.com/problems/sorting-the-sentence/


class Solution:
    def sortSentence(self, s: str) -> str:
        splitted = s.split(" ")
        res = [None]*len(splitted)
        ind = 0

        for i in range(len(splitted)):
            ind = int(splitted[i][-1])-1
            res[ind] = splitted[i][:-1]

        finalStr = " ".join(res)

        return (finalStr)
