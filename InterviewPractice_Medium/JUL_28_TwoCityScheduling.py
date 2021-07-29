# https://leetcode.com/problems/two-city-scheduling/submissions/
"""
1029. Two City Scheduling

A company is planning to interview 2n people. 
Given the array costs where costs[i] = [aCosti, bCosti], 
the cost of flying the ith person to city a is aCosti, 
and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

Key insight: Greedy 
- What would be the "greedy" condition to pick A over B? 
- Think about the price difference between cost[i][0] - cost[i][1]
- Order by A-B or B-A (in ascending order)
- for example, costs = [[10,20],[30,200],[400,50],[30,20]]
- if we do B - A, then we have, 10, 170, -350, -10 (it is -350, -10 cheaper to send those people to B instead of A)
"""


class Solution:
    # more optimized, but there is not much time difference between the below
    # 40ms ~ 36ms, 60% ~ 88%
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # A - B 가 작은 순서대로 (즉 B값과 A 값의 차이가 작 -> 큰 )
        costA = sorted(costs, key=lambda x: x[0] - x[1])
        print(costA)
        res = 0
        for i in range(len(costs)):
            if i < len(costs) // 2:
                # print(costA[i][0])
                res += costA[i][0]
            else:
                # print(costA[i][1])
                res += costA[i][1]

        # print(res)
        return res

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costA = sum([x[0] for x in costs])
        # 좀 더 산술적인 계산.
        # A 대신 B로 갈 기준? 을 명확히 잡기.
        #
        difference = sorted(costs, key=lambda x: x[1] - x[0])
        print(difference, costA)

        for i in range(len(difference)//2):
            costA += difference[i][1] - difference[i][0]

        return costA
