"""
숫자 야구 
https://www.acmicpc.net/problem/2503


민혁이가 말한 세 자리 수에 있는 숫자들 중 하나가 영수의 세 자리 수의 동일한 자리에 위치하면 스트라이크 한 번으로 센다. 
숫자가 영수의 세 자리 수에 있긴 하나 다른 자리에 위치하면 볼 한 번으로 센다.


"""

import sys 
input = sys.stdin.readline

N = int(input())

possible_nums = [True] * 1000 
res = 0 

# falsify impossible values 
def falsifyImpossible(): 
  for i in range(1000):
    if i <= 122 or i >= 988: 
      possible_nums[i] = False 

    string = str(i)
    if len(string) > 2: 
      if string[0] == string[1] or string[0] == string[2] or string[1] == string[2]:
        possible_nums[i] = False 

      if string[0] == "0" or string[1] == "0" or string[2] == "0": 
        possible_nums[i] = False  


def calculateSB(str_num, s, b): 
  for i in range(123, 988): 
    temp_s = 0 
    temp_b = 0 
    
    if possible_nums[i] == True: 
      string_i = str(i) 

      for j in range(3):
        for k in range(3): 
          if j == k and string_i[j] == str_num[k]: 
            temp_s += 1 
          if j != k and string_i[j] == str_num[k]: 
            temp_b += 1 

      if temp_b != b or temp_s != s: 
        possible_nums[i] = False

falsifyImpossible()

for _ in range(N): 
  num, strike, ball = map(int, input().rstrip().split())
  str_num = str(num)

  print(num, strike, ball)

  calculateSB(str_num, strike, ball) 

for i in range(len(possible_nums)): 
  if possible_nums[i] == True: 
      print(i)
      res += 1 

print(res)


"""
3 
123 1 1 
324 0 1 
456 0 0 

2
123 0 0 
456 0 0 

"""

# permutation 사용한 풀이
def v2(): 
  from itertools import permutations

  N = int(sys.stdin.readline())
  ary = []
  table = list(permutations([1,2,3,4,5,6,7,8,9], 3))

  for _ in range(N):
      test, s, b = map(int, sys.stdin.readline().split())
      test = list(str(test))
      remove_cnt = 0

      for i in range(len(table)):
          s_cnt = b_cnt = 0
          i -= remove_cnt

          for j in range(3):
              test[j] = int(test[j])
              if test[j] in table[i]:
                  if j == table[i].index(test[j]):
                      s_cnt += 1
                  else:
                      b_cnt += 1

          if s_cnt != s or b_cnt != b:
              table.remove(table[i])
              remove_cnt += 1

  print(len(table))
    








