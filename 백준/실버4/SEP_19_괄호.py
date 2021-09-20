"""
괄호 

https://www.acmicpc.net/problem/9012

valid parenthesis 

"""
import sys 
input = sys.stdin.readline

N = int(input())

# using stack ds
def isParenValid(string): 
  stack = [] 

  for el in string: 
    if el == "(": 
      stack.append("(")
    
    elif el == ")": 
      if stack and stack[-1] == "(": 
        stack.pop() 
      else: 
        print("NO")
        return False 
  
  if stack: 
    print("NO")
    return False 
  else: 
    print("YES")
    return True 

# no need to use stack ds. 
# can do with number! 
def isParenValid_V2(string): 
  stack = 0 

  for char in string: 
    if char == "(": 
      stack += 1 
    else: 
      stack -= 1 

      if stack < 0: 
        break 
  
  if stack == 0: 
    print("YES")
  else: 
    print("NO")
    
for _ in range(N): 
  string = input()
  isParenValid_V2(string)


      

