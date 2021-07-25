import heapq


class Solution:

    # Very slow. 5.03%
    # O(n^2)
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1:
            return 0

        sortedSticks = sorted(sticks, reverse=True)
        end = len(sortedSticks) - 1
        end2 = end - 1
        total = 0

        while len(sortedSticks) > 0:
            # print(sortedSticks)
            newel = sortedSticks[end] + sortedSticks[end2]
            total += newel
            # print(total)
            sortedSticks.pop()
            if len(sortedSticks) == 1:
                return total
            sortedSticks.pop()
            sortedSticks.append(newel)
            sortedSticks.sort(reverse=True)
            end = len(sortedSticks) - 1
            end2 = end - 1

        print(sortedSticks)

    # 300ms, 92.39  (o(n))
    # Key Insight: be more familiar with heapq!
    def connectSticks_heapq(self, sticks: List[int]) -> int:
        if len(sticks) == 1:
            return 0

        heapq.heapify(sticks)
        res = 0

        while len(sticks) > 1:
            newEl = heapq.heappop(sticks) + heapq.heappop(sticks)
            res += newEl
            heapq.heappush(sticks, newEl)

        return res
