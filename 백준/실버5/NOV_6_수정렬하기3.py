""" 
https://www.acmicpc.net/problem/10989

수 정렬하기 3 

Key Idea: 
- 모든 원소를 받아서 입력을 하면 메모리 초과가 난다. 
- 받은 수의 갯수를 배열에 저장하고 
- 배열을 앞에서부터 순서대로 갯수만큼 배열의 index 번호를 출력하면 된다. 

"""

import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = [0] * 100001

for i in range(N):
    n = int(input().rstrip())
    nums[n] += 1


def sortAndPrint():
    for i in range(len(nums)):
        for _ in range(nums[i]):
            print(i)


sortAndPrint()
