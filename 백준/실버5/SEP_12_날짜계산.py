"""
날짜 계산 

Key Insight: 
- 수학을 사용해야 한다. 
- x 가 찾으려는 십진법 년도일때, 
- E, S, M 에 각각 맞는 식을 세워야 한다. (자세한 것은 직접 날짜를 적어서 E,S,M 으로 표현해보면 이해가 쉽다.)
- 1) E 달력은, 
      x = 15E + 주어진 E 날짜 
  2) S 
      x = 28S + 주어진 S 날짜 
  3) M 
      x = 19w + 주어진 M 날짜 

  로 표현이 가능하다. 

- 이때, x 를 기준으로 답을 구한다 (*** 공통으로 많이 사용되는 미지수를 먼저 구한다)
- 방식은 brute force 하게 1 (1 인 이유: 0년은 없다) 부터 E,S,M 의 조건이 모두 성립할 때 까지 1 씩 추가하면서 답을 구한다.
"""


def calculateDate(y1, y2, y3):
    x = 1
    while True:
        if ((x - y1) % 15 == 0) and ((x - y2) % 28 == 0) and ((x - y3) % 19 == 0):
            print(x)
            return
        x += 1


E, S, M = map(int, input().split())
calculateDate(E, S, M)
