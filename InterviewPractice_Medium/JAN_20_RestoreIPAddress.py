"""
https://leetcode.com/problems/restore-ip-addresses/

Restore IP Address

DFS 
"""


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def dfs(ind, depth, ip):
            # 종료 조건: 4개의 subnet 그리고 길이가 s 와 같을때, 종료
            if depth == 4:
                if ind == len(s):
                    res.append(ip[:])
                return

            for i in range(ind + 1, ind + 4):
                # 1.xxx.xxx.xxx 와 같이 한 자리 서브넷
                subnet = s[ind:i]

                intSubnet = 0
                if subnet == "":
                    intSubnet = 0
                else:
                    intSubnet = int(subnet)

                # 올바른 서브넷
                # 255 이하, 023, 001 과 같이 2자리수 혹은 한자리수 앞에 0이 붙지 않는다.
                if len(subnet) >= 2 and subnet[0] == 0:  # ??????
                    continue
                elif intSubnet <= 255:
                    # 마지막 서브넷이면 점을 추가하지 않는다.
                    if depth + 1 == 4:
                        dfs(i, depth + 1, ip + subnet)
                    else:
                        dfs(i, depth + 1, ip + subnet + ".")

        dfs(0, 0, "")
        return res
