"""
https://leetcode.com/problems/insert-interval/

Insert Interval

"""


from typing import List


class Solution:
    """
    approach : 

    start with cur 
    check for overlap, 

    if not overlap, 
    add to result 

    else 
    start merging 

    """

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        cur = 0
        next = cur

        while cur < len(intervals):
            curVal = intervals[cur]
            nextVal = intervals[next]

            # if start value of the new interval is in the between the
            # start value of the curVal, and the end value of the curVal sub-interval
            if curVal[0] <= newInterval[0] <= curVal[1]:
                nextVal = intervals[cur+1]

                intervals[cur][0] = min(newInterval[0], curVal[0])
                intervals[cur][1] = max(newInterval[1], curVal[1])

                newInterval = intervals[cur]
