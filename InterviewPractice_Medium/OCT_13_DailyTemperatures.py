""" 
https://leetcode.com/problems/daily-temperatures/

decreasing monotone stack. 
contents of stack: 
  stack[actualTemperature][day]

- from the current day (i), append to res if top el of stack is less than current day's temp. 
- position in the res array: poppedElDay(stack.pop()[1] = day of a temp)
- contents in the res array: currentDay(i) - poppedElDay(stack.pop()[1] = day of a temp)


"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # decreasing monotone stack 
        stack = [] 
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures)): 
            el = temperatures[i]
            while stack and stack[-1][0] < el: 
                popped = stack.pop()
                days = i - popped[1]                   
                res[popped[1]] = days

            stack.append([el, i]) 
        
        return res 
    
    def dailyTemperaturesV2(self, temperatures: List[int]) -> List[int]:
      stack = [] 
      res = [0] * len(temperatures)

      for i, curT in enumerate(temperatures): 
        while stack and curT > temperatures[stack[-1]]: 
          last = stack.pop() 
          res[last] = i - last 
        stack.append(i)