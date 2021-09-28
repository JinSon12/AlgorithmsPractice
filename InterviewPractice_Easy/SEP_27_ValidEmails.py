"""
Unique Email Addresses

https://leetcode.com/problems/unique-email-addresses/submissions/

조건에 맞추어 
unique 한 이메일 주소를 set 를 사용하여서 찾는다. 

"""


class Solution:
    def numUniqueEmails_mostConcise(self, emails: List[str]) -> int:
        fixed = set()
        for em in emails:
            name, domain = em.split('@')
            if '+' in name:
                name, _ = name.split('+', 1)
            name = name.replace('.', '')
            fixed.add(name + '@' + domain)
        return len(fixed)

    def numUniqueEmails_dictionary(self, emails: List[str]) -> int:
        d = {}
        
        for email in emails: 
            name, addr = email.split("@")
            
            cleanName = ""
            for char in name: 
                if char == ".": 
                    continue 
                if char == "+":
                    break 
                else: 
                    cleanName += char 
            
            if addr not in d: 
                d[addr] = [cleanName]
            else: 
                d[addr].append(cleanName)
        
        cnt = 0 
        for v in d.values(): 
            sv = len(set(v))
            cnt += sv
        
        return cnt 
            
    def numUniqueEmails_set(self, emails: List[str]) -> int:
        d = set()
        
        for email in emails: 
            name, addr = email.split("@")
            
            cleanName = ""
            for char in name: 
                if char == ".": 
                    continue 
                if char == "+":
                    break 
                else: 
                    cleanName += char 
            
            d.add(cleanName + "@" + addr)
        
        print(d)
        return len(d)
            