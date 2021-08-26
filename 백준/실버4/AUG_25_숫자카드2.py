"""
숫자 카드 2. 

- defaultDict 
- counter 

"""
from collections import defaultdict
import sys

input = sys.stdin.readline
N = input()
allCards = sorted(map(int, input().split()))
M = input()
cardsToLookFor = map(int, input().split())


def findNumber(allCards, cardsToLookFor):
    d = defaultdict(int)
    for card in allCards:
        d[card] += 1

    print(" ".join(str(d[card])
                   if card in d else '0' for card in cardsToLookFor))


findNumber(allCards, cardsToLookFor)
