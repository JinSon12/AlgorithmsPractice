"""
팩토리얼 0의 갯수

수학


소인수 분해를 해 보기 
- 뒷자리에 0 이 있다는 것은 
- 2 * 5 가 있다는 것. 
- 5의 갯수가 중요하다 (이것은 소인수 분해를 해 보면 안다. 2가 5 보다 훨씬더 많다.)
"""


def findZero(num):
    n = 1
    count = 0

    for i in range(1, num + 1):
        n *= i

        while num >= 5:
            count += num // 5
            num //= 5

    print(n, count)


findZero(60)
