"""
Making File Names Unique

https://leetcode.com/problems/making-file-names-unique/

"""


from typing import List

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        res = []
        d = {}

        for name in names:
            if name not in d:
                res.append(name)
                d[name] = 1

            else:
              # 만약 주어진 이름이 이미 존재 한다면, 
              # 새 이름 만들기. 
              # 그리고 다음 넘버링을 위해 1 추가. 
                newname = name + "(" + str(d[name]) + ")"
                d[name] += 1

                # 새 이름이 이미 존재하는지 확인. 
                # 존재한다면, 새로운 숫자를 주고, 
                # 넘버링을 1 추가 한다. 
                while newname in d: 
                    newname = name + "(" + str(d[name]) + ")"
                    d[name] += 1
                    
                # 새 이름이 d 에 없다면, 
                # 결과에 추가하고, 
                # 새 이름을 d 에 저장하여, 다음 번에 있는지 없는지 확인할 때 사용한다. 
                res.append(newname)
                d[newname] = 1

        return res

stn = Solution() 
stn.getFolderNames(["gta","gta(1)","gta","avalon"])