# https://leetcode.com/problems/maximum-units-on-a-truck/submissions/

class Solution:

    """
    Key Insights: 
    - when to use DP vs. Greedy? 
      - 부분 최적해가 전체 최적해를 만족한다면 DP (작은 부분부분의 최선의 선택은 전체적으로 최선의 선택일 것)
      - Greedy : 선택의 순간에서 가장 좋은 선택을 하자. (하지만 결과는 모른다)
    - 굳이 DP 를 사용하지 않아도 된다 (연산량이 많아지므로, 시간이 더 걸린다)
    - Greedy는 Global Optima 를 찾아주지는 않지만, 속도는 빠르다. 

    https://rain-bow.tistory.com/entry/DP와-Greedy-Algorithm
    """
    # first try! 98.93% faster than other solutions. :D

    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        maxw = truckSize
        totalu = 0

        boxTypes.sort(key=(lambda x: x[1]), reverse=True)

        for i in boxTypes:
            w = i[0]
            units = i[1] * w

            if maxw - w < 0:
                return totalu + i[1] * maxw

            maxw -= w
            totalu += units

        return totalu
