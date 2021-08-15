# https://leetcode.com/problems/merge-intervals/

""" 
56. Merge Intervals 


"""


class Solution:
    # 100ms - 15%
    """
    IDEA : 
    - sort the array in regards to the first element interval[x][0] 
    - compare prev and cur element 
    - find the localmin and local max, in the prev, and cur element 
    - if prev[1] >= cur[0] (cur 0 is smaller than prev1) 
        - => they overlap. 
        - new array of [localmin, localmax]
        - change the interval array 
        - decrease the pointer by 1 (so that the position stays the same, if not, pointer could get longer than the len of updated intervals)

    """

    def merge_v1(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        temp = []

        # sort the array in regards to the first element interval[x][0]
        intervals.sort(key=lambda x: (x[0], x[1]))

        p = 1
        while p < len(intervals):
            prev0 = intervals[p-1][0]
            prev1 = intervals[p-1][1]
            cur0 = intervals[p][0]
            cur1 = intervals[p][1]

            localmin = min(prev0, prev1, cur0, cur1)
            localmax = max(prev0, prev1, cur0, cur1)

            if prev1 >= cur0:
                intervals[p-1:p+1] = [[localmin, localmax]]
                p -= 1

            p += 1

        return intervals

    """
    improvements: 

    - key idea similar to v1 
    - instead of changing the intervals array directly, 
    - modified the temp array. 

    """

    def merge_v2(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        temp = []

        intervals.sort(key=lambda x: (x[0], x[1]))

        p = 1
        while p < len(intervals):
            prev0 = intervals[p-1][0]
            prev1 = intervals[p-1][1]
            cur0 = intervals[p][0]
            cur1 = intervals[p][1]

            localmin = min(prev0, prev1, cur0, cur1)
            localmax = max(prev0, prev1, cur0, cur1)
            # print(p, intervals, temp)

            """
            change 
            """
            if prev1 >= cur0:
                # print(p, prev1, cur0)
                intervals[p][0] = localmin
                intervals[p][1] = localmax

                if temp and temp[-1][0] == localmin:      # if the smaller elements
                    temp.pop()

                temp.append([localmin, localmax])
                # p -= 1
                # print(temp)
            else:
                if p == 1:
                    # print(intervals[:2])
                    temp += intervals[:2]
                else:
                    temp.append(intervals[p])

            p += 1

        return temp

    # same idea, but different implementation (faster way, concise way to implement)
    def merge_fastest(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda interval: interval[0])
        result = []
        interval, l = intervals[0], len(intervals)

        for i in range(1, l):
            interval2 = intervals[i]
            if interval2[0] > interval[1]:
                result.append(interval)
                interval = interval2
            else:
                interval[1] = max(interval[1], interval2[1])

        result.append(interval)
        return result

    # 72ms solution
    # cleaner implementation
    def merge_faster(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals = sorted(intervals, key=lambda x: x[0])
        merged_intervals = []

        for interval in intervals:
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)

            else:
                merged_intervals[-1][1] = max(merged_intervals[-1]
                                              [1], interval[1])
        return merged_intervals
