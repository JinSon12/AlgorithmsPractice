class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strDig = "".join([str(num) for num in digits])

        newDig = str(int(strDig)+1)

        newDiglist = [int(x) for x in newDig]

        return (newDiglist)
