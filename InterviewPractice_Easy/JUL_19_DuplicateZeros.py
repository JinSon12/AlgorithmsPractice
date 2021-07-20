class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # space: O(n), time: O(n)
        temp = []

        for i in arr:
            if i == 0:
                temp.append(0)
            temp.append(i)

        for i in range(len(arr)):
            arr[i] = temp[i]

        return arr

    def duplicateZeros_V2(self, arr):
        length = len(arr)
        cntZero = arr.count(0)
        j = length + cntZero - 1
        i = length - 1

        while(j >= 0):
            if j < length:
                arr[j] = arr[i]
            j -= 1
            if arr[i] == 0:
                if j < length:
                    arr[j] = arr[i]
                j -= 1
            i -= 1
