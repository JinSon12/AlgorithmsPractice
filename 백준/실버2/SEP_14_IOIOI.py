"""
IOIOI

https://www.acmicpc.net/problem/5525

- 슬라이딩 윈도우를 사용해서 알파벳 갯수만큼이 배열에 저장되어 있는 수를 빼고 추가하고는
  여기서 쓸 수 없다. 
  - 그 알고리즘 자체가 anagram (즉, 철자의 배치 순서 상관없이 철자의 갯수만 새면 되는 것이기 때문이다.)
  - 하지만, 이 경우에는 순서와 갯수 모두 중요하다. (IOI와 같이) 아나그램일 경우 (IIO, IOI 상관 없었을 것이다.)


"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
S = input()


def buildN():
    string = "I"

    for _ in range(N):
        string += "OI"

    return string


string = buildN()

# 50 점. 즉, N ≤ 100, M ≤ 10 000. 일때 정상 작동.


# 그냥 세기.
# IOI 의 갯수를 그냥 세면 된다. (즉, pos, pos+1, pos+2 까지 확인하면 되는 것)
# 단, IOI 조건이 성립한다면, 두칸씩 뛰어서 검사를 진행하면 된다.
def findOccurences(S, string):
    left = 0
    temp = 0
    counter = 0
    L = len(string)

    while left + 2 < len(S):
        if S[left] == "I" and S[left + 1] == "O" and S[left + 2] == "I":
            temp += 1

            if temp == N:
                counter += 1
                temp -= 1

            left += 1
        else:
            temp = 0

        left += 1

    print(counter)


findOccurences(S, string)
