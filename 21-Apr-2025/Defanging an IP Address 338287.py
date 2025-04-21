# Problem: Defanging an IP Address - https://leetcode.com/problems/defanging-an-ip-address/description/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        res=[]
        for char in address:
            if char==".":
                res.append("[.]")
            else:
                res.append(char)
        return "".join(res)
        