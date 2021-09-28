"""
Simplify path

https://leetcode.com/problems/simplify-path/

The main idea is to push to the stack every valid file name (not in {"",".",".."}), 
popping only if there's smth to pop and we met "..". 

"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = [] 
        
        res = ""
        for i in range(len(paths)): 
            char = paths[i]
            if char != "": 
                if char == "..":
                    if stack: 
                        stack.pop() 
                elif char.isalnum() or (char != ".." and char != "."):         
                    stack.append(char)
        
        # 앞에 / 를 기본으로 추가한 후, 
        # 각 원소마다 "/" 를 추가한다. 
        return "/" + "/".join(stack)
   
    def simplifyPath_v2_moreConcise(self, path: str) -> str:
        op = ''
        stack = []
        for p in path.split('/'):
            if not p:
                continue
            if p == '.':
                continue
            if p == '..':
                if stack:
                    stack.pop()
                continue
            stack.append(p)

        return '/' + '/'.join(stack)
            
            