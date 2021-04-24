# In a given string s, return True if occurances of P and Y are the same. If none, return True 
# if not the same, return False. 

# for some reason, .lower() did not pass all the tests. why? 
def solution(s):
    countp = 0 
    county = 0 
    countp = s.count("p") + s.count("P")
    county = s.count("y") + s.count("Y")

    if countp == county : 
        return True 
    else : 
        return False

# simpler solution 
# import Counter object. 
import collections import Counter 

def solutionSimple(s): 
  c = Counter(s.lower()) 
  return c['y'] == c['p'] 
