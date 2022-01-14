""""
https://leetcode.com/problems/angle-between-hands-of-a-clock/

1. 시침의 각도 계산 
2. 분침의 각도 계산 
3. 시침과 분침 사이의 각도 = |시침의 각도 - 분침의 각도| 

예제 1. 12:30 
시 : 15도 
분 : 180도 
각 : 165 (각이 360 - 각 보다 작다.)

ex 2. 3:30 
시 : (3 * 30 + 30 * 0.5) = 105
분 : 180 
각 : 180 - 105 = 75 (다른 편의 각도는 285)

ex 3. 10:10 
시 : (30 * 10 + 0.5 * 10) = 305 
분 : 6 * 10 = 60 
각 : 305 - 60 = 245 (다른 각 : 115)



경우 
1) 시침과 분침의 각도가 예각인 경우 
    - 각 
2) 시침과 분침의 각도가 180이 넘는 경우 
    - 360 - 각 

- 시침의 각도 구한다 
- 분침의 각도 구한다 
- 시침 - 분침의 절댓값을 구한다 
- 결과 = 0 
- 경우를 따진다. 
  - 경우 1. 
    결과 = 각
  - 경우 2. 
    결과 = 360 - 각 

혹은 min 함수 사용 가능. 
min(경우 1의 결과, 경우 2의 결과)  

"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = 30 * hour + 0.5 * minutes
        m = 6 * minutes
        diff = abs(h-m)

        res = 0
        if diff > 180:
            res = 360 - diff
        else:
            res = diff

        return res
