# https://leetcode.com/problems/relative-sort-array/

from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d1 = Counter(arr1)
        result = []

        for i in arr2:
            while i in d1 and d1[i] > 0:
                result.append(i)
                d1[i] -= 1
            d1.pop(i)

        for k in (sorted(d1.keys())):
            for j in range(d1[k]):
                result.append(k)

        return result

    def relativeSortArray_V3(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(sorted(arr1))  # arr1 을 정렬후 카운트
        ans = []

        for i in arr2:   # arr2의 값들을 순서대로 대입
            for j in range(count[i]):   # 이번 차례의 arr2의 원소가 arr1에 들어있는 만큼 반복
                ans.append(i)            # 정답에 추가
                count[i] -= 1            # 카운트 개수 -1
        # arr2에 있는 값들대로는 정렬 완료 후 , 나머지 추가
        # elements() 함수는 Counter class 에 있는 함수.
        # returns all the elments in the Counter object.
        # https://www.geeksforgeeks.org/python-counter-objects-elements/
        # {2:1, 3:2} => 2 3 3
        return ans + list(count.elements())

    def relativeSortArray_V4(self, arr1, arr2):
        c = collections.Counter(arr1)
        res = []
        for i in arr2:
            res += [i]*c.pop(i)
        return res + sorted(c.elements())

    # re-written from https://leetcode.com/problems/relative-sort-array/discuss/334570/JavaPython-3-O(max(n2-N))-code-similar-to-791-Custom-Sort-String.
    def relativeSortArray_V5_Non_PythonicWay(self, arr1: List[int], arr2: List[int]) -> List[int]:
        rInd = 0
        result = [None]*len(arr1)
        ind = [0]*1001

        for i in arr1:
            ind[i] += 1

        for i in arr2:
            while(ind[i] > 0):
                result[rInd] = i
                rInd += 1
                ind[i] -= 1

        for i in range(len(ind)):
            while(ind[i] > 0):
                result[rInd] = i
                rInd += 1
                ind[i] -= 1

        return(result)

    def relativeSortArray_V2(self, arr1, arr2):
        r = []  # Hold the resulting relative sort array
        m = {}  # Used for counting elements of arr2 that appear in arr1
        diff = []  # Use for tracking elements that don't appear in arr2 but appear in arr1

        # Initialize counts
        for num in arr2:
            if num not in m:
                m[num] = 0

        for num in arr1:
            if num in m:
                m[num] += 1  # Increment count of elements seen
            else:
                # Add element to difference list (e.g. nums in arr1 not in arr2)
                diff.append(num)

        diff.sort()  # Sort the difference

        for num in arr2:
            # Add the number of elements seen to  the result set
            # extend vs append (O(n) vs O(1)):
            # so this loop would be O(n^2)
            # https://www.geeksforgeeks.org/append-extend-python/
            r.extend([num] * m[num])

        r.extend(diff)  # Add the rest of the sorted elements

        return r
