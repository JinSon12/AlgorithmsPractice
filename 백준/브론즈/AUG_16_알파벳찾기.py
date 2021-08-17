"""
10809. 알파벳 찾기 

"""


def findAlpha(s):
    d = {}
    curOrd = ord("a")

    for i in range(curOrd, curOrd+26):
        curChar = chr(i)
        d[curChar] = -1

    for ind, char in enumerate(s):
        if d[char] == -1:
            d[char] = ind

    print(*d.values())


def findAlpha_list(s):
    s = input().strip()
    ans = [-1 for _ in range(26)]

    # 중복 등장하는 글자가 있더라도 뒤에서부터 탐색하기때문에 무조건 앞에 등장한 글자의 포지션을 저장하게 된다.
    for i in range(len(s) - 1, -1, -1):
        ans[ord(s[i]) - ord('a')] = i

    print(*ans)


findAlpha(input())
