class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def comparer(s): 
            res = []

            for i in s: 
                if i == "#":
                    if res:         # when checking for array/stack length, use name, not len(name) > 0, much faster this way 
                        res.pop()
                elif i != "#": 
                    res.append(i)
            
            return res
        
        return comparer(s) == comparer(t)
        