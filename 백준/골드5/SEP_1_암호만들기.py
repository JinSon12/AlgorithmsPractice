"""
암호만들기 
https://www.acmicpc.net/problem/1759

암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다. 
또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다. 
즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.

새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다. 
이 알파벳을 입수한 민식, 영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다. 
C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.

4 6
a t c i s w
-> 
acis
acit
aciw
acst
acsw
actw
aist
aisw
aitw
astw
cist
cisw
citw
istw
"""

from itertools import combinations
import sys
input = sys.stdin.readline

L, C = map(int, input().split())
s = input().split()


def findCombinationLetter(s, target):
    res = []
    vowels = set({"a", "e", "i", "o", "u"})

    s.sort()

    def dfs(pos, sSoFar, cntV, cntC):
        if len(sSoFar) == target and cntV >= 1 and cntC >= 2:
            res.append(sSoFar)
            return

        for i in range(pos, len(s)):
            if s[i] in vowels:
                dfs(i + 1, sSoFar + s[i], cntV + 1, cntC)
            else:
                dfs(i + 1, sSoFar + s[i], cntV, cntC + 1)

    dfs(0, "", 0, 0)

    return res


print(findCombinationLetter(s, L))


# using combination tools, 속도차이는 크게 없다.
def combinationString():
    vowles = set({'a', 'e', 'i', 'o', 'u'})

    def alpha(s):
        value = 0
        for i in s:
            if i in vowles:
                value += 1
        return value

    # among all the combinations created by the function, with string s, and length L
    for i in combinations(s, L):
        if alpha(i) >= 1 and (len(i) - alpha(i)) >= 2:
            print(''.join(i))
